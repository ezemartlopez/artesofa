from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:5173"}})


# Ejemplo de productos
productos = [
    {
        "id":13,
        "name": "TOKIO",
        "description":"EL VALOR PUBLICADO CORRESPONDE A LA MEDIDA DE 200x090 Consultanos su valor en otras medidas: 1.40 / 1.50 / 1.60 / 1.80 / 1.90 / 2.00 / 2.20 / 2.30 / 2.50 / f...",
        "price":"612700",
        "cash_price":"490160",
        "image_primary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/edit-28-06_511-1b146451f9b550c78716606637592613-640-0.webp",
        "image_secondary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/edit-28-06_501-24a0b304c3b3fcbeab16606637593844-640-0.webp",
        "type": "sofas"
      },
      {
        "id":14,
        "name":"CHESTER CONSTRUCTOR",
        "description":"EL VALOR PUBLICADO CORRESPONDE A LA MEDIDA DE 3 CUERPOS *Adicionales en la foto no incluidos en el valor: Placa Soft de 28 Consultanos su valor en otras me...",
        "price":"774800",
        "cash_price":"619840",
        "image_primary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/edit-23-06-241-2faf17fc7a8eb48f5c16560822791164-640-0.webp",
        "image_secondary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/edit-23-06-281-55301f6ae7a3ecb21e16560822792794-640-0.webp",
        "type": "sofas"
      },
      {
        "id":15,
        "name":"SANTORINI",
        "description":"EL VALOR PUBLICADO CORRESPONDE A LA MEDIDA DE 200X090 *Adicionales en la foto no incluidos en el valor: Tapizado Panne antimanchas Consultanos su valor en ot...",
        "price":"634400",
        "cash_price":"507520",
        "image_primary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/edit-02-08_301-ae890b5ed97472cb9e16596308435907-640-0.webp",
        "image_secondary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/edit-02-08_311-97b28ca525d96651f516596308531025-640-0.webp",
        "type": "sofas"
      },
      {
        "id":16,
        "name":"MOSCÚ",
        "description":"EL VALOR PUBLICADO CORRESPONDE A LA MEDIDA DE 160x090 *Adicionales en la foto no incluidos en el valor: Tapizado Panne antimanchas Consultanos su valor en ot...",
        "price":"541100",
        "cash_price":"432880",
        "image_primary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/edit-02-08_39_cuadro1-6fb6b345d1aca5ba8a16596306381520-640-0.webp",
        "image_secondary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/edit-02-08_40_cuadro1-8881185655be10598c16596306460708-640-0.webp",
        "type": "sofas"
      },
      {
        "id":17,
        "name":"VICTORIA",
        "description":"EL VALOR PUBLICADO CORRESPONDE A LA MEDIDA DE 200x090 *Adicionales en la foto no incluidos en el valor: Tapizado Panne antimanchas Consultanos su valor en ot...",
        "price":"612700",
        "cash_price":"490160",
        "image_primary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/edit-28-06_291-f64cb05e1dd74c068d16607387111147-640-0.webp",
        "image_secondary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/edit-28-06_281-c2b5e9ffc9788156e316607387109984-640-0.webp",
        "type": "sofas"
      },
      {
        "id":18,
        "name":"MISSOURI",
        "description":"EL VALOR PUBLICADO CORRESPONDE A LA MEDIDA DE 200X090 Consultanos su valor en otras medidas: 1.40 / 1.50 / 1.60 / 1.80 / 1.90 / 2.20 / 2.30 / 2.50 / formato ...",
        "price":"645800",
        "cash_price":"516640",
        "image_primary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/edit-25-08_641-4ada4f83018b0b0c0d16618748501664-640-0.webp",
        "image_secondary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/edit-25-08_631-eb12c22c6ca9fff96416618748502286-640-0.webp",
        "type": "sofas"
      },
      {
        "id":19,
        "name":"CAROL",
        "description":"EL VALOR PUBLICADO CORRESPONDE A LA MEDIDA DE 1.80X0.90 *Adicionales en la foto no incluidos en el valor: Mojito antimanchas Consultanos su valor en otras me...",
        "price":"572200",
        "cash_price":"457760",
        "image_primary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/edit-25-08_381-9fd9026517ae79e94616618749712729-640-0.webp",
        "image_secondary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/edit-25-08_391-04b91fe19b1c93ef8116618749713134-640-0.webp",
        "type": "sofas"
      },
      {
        "id":20,
        "name":"CHICAGO",
        "description":"EL VALOR PUBLICADO CORRESPONDE A LA MEDIDA DE 200x090 *Adicionales en la foto no incluidos en el valor: Base de madera Consultanos su valor en otras medidas:...",
        "price":"612700",
        "cash_price":"490160",
        "image_primary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/edit-05-07_221-54032add78e5d902c016570461554140-640-0.webp",
        "image_secondary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/edit-05-07_211-2ee2bc08e5e2d1411d16570461554020-640-0.webp",
        "type": "sofas"
      },
      {
        "id":21,
        "name":"VERONA",
        "description":"EL VALOR PUBLICADO CORRESPONDE A LA MEDIDA DE 200x090 *Adicionales en la foto no incluidos en el valor: Base de madera Consultanos su valor en otras medidas:...",
        "price":"612700",
        "cash_price":"490160",
        "image_primary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/edit-07-09_11-21386938fdfcc5925816626504477757-640-0.webp",
        "image_secondary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/edit-07-09_21-00529c49743d9b58e416626504477060-640-0.webp",
        "type":"sofas"
      },
      {
        "id":22,
        "name":"LOS ANGELES",
        "description":"EL VALOR PUBLICADO CORRESPONDE A LA MEDIDA DE 220x100 &nbsp; Consultanos su valor en otras medidas: 2.00 / 2.50 /&nbsp;formato esquinero ¿Que opciones&nbsp;incluyen los pre...",
        "price":"719000",
        "cash_price":"632800",
        "image_primary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/edit-91-de686cd3b907d22e1216560825019185-640-0.webp",
        "image_secondary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/edit-101-4a13a720e4b336c97116560825024664-640-0.webp",
        "type":"sofas"
      },
      {
        "id":23,
        "name":"ROMA",
        "description":"EL VALOR PUBLICADO CORRESPONDE A LA MEDIDA DE 1.80X0.80 *Adicionales en la foto no incluidos en el valor: Panne antimanchas Consultanos su valor en otras med...",
        "price":"572200",
        "cash_price":"457760",
        "image_primary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/image-21-e6fce4b9671b35b83d16855427600729-640-0.webp",
        "image_secondary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/image1-9a7d74992c6d099fd816855427591448-640-0.webp",
        "type":"sofas"
      },
      {
        "id":24,
        "name":"CHESTER CLÁSICO",
        "description":"EL VALOR PUBLICADO CORRESPONDE A LA MEDIDA DE 3 CUERPOS Consultanos su valor en otras medidas:&nbsp;1 / 2 / 4 cuerpos / formato esquinero ¿Que opciones&nbsp;incluyen l...",
        "price":"724700",
        "cash_price":"579760",
        "image_primary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/edit-21-07_2211-a9cc2dd00131d9285416585251984400-640-0.webp",
        "image_secondary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/edit-21-07_2311-c07c2342a1df63ae9616585251987141-640-0.webp",
        "type":"sofas"
      },
      {
        "id":25,
        "name":"VINTAGE",
        "description":"EL VALOR PUBLICADO CORRESPONDE A LA MEDIDA DE 1.60X0.90 Consultanos su valor en otras medidas: 1.40 / 1.50 / 1.80&nbsp;/ 2.00 /&nbsp;1.90&nbsp;/ 2.20 / 2.30 / 2.50 / format...",
        "price":"557400",
        "cash_price":"445920",
        "image_primary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/edit-23-06-101-6f4e7466085dcf32aa16564402812932-640-0.webp",
        "image_secondary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/edit-23-06-121-46daaa088a8e3d4a1416564402817072-640-0.webp",
        "type":"sofas"
      },
      {
        "id":26,
        "name":"DUBLIN",
        "description":"EL VALOR PUBLICADO CORRESPONDE A LA MEDIDA DE 2.00x0.90 *Adicionales en la foto no incluidos en el valor: Base de madera Consultanos su valor en otras medi...",
        "price":"612700",
        "cash_price":"490160",
        "image_primary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/edit-23-06-171-a13ad2efb4e13cbe1d16563314541258-640-0.webp",
        "image_secondary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/edit-23-06-161-7f9abf3a05cff9999716563314538682-640-0.webp",
        "type":"sofas"
      },
      {
        "id":27,
        "name":"ATHENAS",
        "description":"EL VALOR PUBLICADO CORRESPONDE A LA MEDIDA DE 250X090 *Adicionales en la foto no incluidos en el valor: Tapizado Panne antimanchas Consultanos su valor en ot...",
        "price":"740300",
        "cash_price":"592240",
        "image_primary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/edit-28-06_581-036c006aa8104d869516606636785472-640-0.webp",
        "image_secondary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/edit-28-06_571-9d32a8a37720a61b6c16606636788233-640-0.webp",
        "type":"sofas"
      },
      {
        "id":28,
        "name":"MANHATTAN",
        "description":"EL VALOR PUBLICADO CORRESPONDE A LA MEDIDA DE 160x090 *Adicionales en la foto no incluidos en el valor: Tapizado Panne antimanchas Consultanos su valor en ot...",
        "price":"557400",
        "cash_price":"445920",
        "image_primary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/_dsc0302-web1-3eb49ca11a8cfb7c4d16560825884046-640-0.webp",
        "image_secondary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/_dsc0304-web1-a38fac66ddf422189716560825885104-640-0.webp",
        "type":"sofas"
      },
      {
        "id":29,
        "name":"ISABEL",
        "description":"EL VALOR PUBLICADO CORRESPONDE A LA MEDIDA DE 1.80X0.90 CON TACHAS Consultanos su valor en otras medidas: 1.40 / 1.50 / 1.60 / 2.00 /&nbsp;1.90&nbsp;/ 2.20 / 2.30 / 2....",
        "price":"592227",
        "cash_price":"473871",
        "image_primary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/edit-07-09_151-d3439962aec8e148a016626503669619-640-0.webp",
        "image_secondary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/edit-07-09_161-d0f716bc76c88108ec16626503673599-640-0.webp",
        "type":"sofas"
      },
      {
        "id":30,
        "name":"LONDON",
        "description":"EL VALOR PUBLICADO CORRESPONDE A LA MEDIDA DE 1.80X0.90 *Adicionales en la foto no incluidos en el valor: Tapizado Panne antimanchas Consultanos su valor e...",
        "price":"572200",
        "cash_price":"457760",
        "image_primary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/image-71-bca2166b2f0f9eb39e16855426962663-640-0.webp",
        "image_secondary":"https:/dcdn.mitiendanube.com/stores/001/271/935/products/image-61-9a949d302718dad10f16855426963865-640-0.webp",
        "type":"sofas"
      },
      {
        "id":31,
        "name":"ZEUS",
        "description":"EL VALOR PUBLICADO CORRESPONDE A LA MEDIDA DE 1.90X0.90 Consultanos su valor en otras medidas: 1.40 / 1.50 / 1.60 / 2.00 /&nbsp;1.80 / 2.20 / 2.30 / 2.50 / form...",
        "price":"596400",
        "cash_price":"477120",
        "image_primary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/edit-02-08_231-f3e0effb1e33ca986216595585512830-640-0.webp",
        "image_secondary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/edit-02-08_241-f0a8c32cd9862a551816595585514640-640-0.webp",
        "type":"sofas"
      },
      {
        "id":32,
        "name":"LUXURY",
        "description":"EL VALOR PUBLICADO CORRESPONDE A LA MEDIDA DE 200x100 Consultanos su valor en otras medidas: 2.20 / 2.50&nbsp;/ formato esquinero &nbsp; ¿Que opciones&nbsp;incluyen los pre...",
        "price":"715600",
        "cash_price":"572480",
        "image_primary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/edit-05-07_21-c3d1d8a0cd766704b616570452470039-640-0.webp",
        "image_secondary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/edit-05-071-4e4ac21d737711ad8816570452468596-640-0.webp",
        "type":"sofas"
      },
      {
        "id":33,
        "name":"DALI",
        "description":"EL VALOR PUBLICADO CORRESPONDE A LA MEDIDA DE 1.80X0.90 Consultanos su valor en otras medidas: 1.40 / 1.50 / 1.60 / 2.00 /&nbsp;1.90&nbsp;/ 2.20 / 2.30 / 2.50 / format...",
        "price":"637300",
        "cash_price":"509840",
        "image_primary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/edit-23-06-31-34e6427d4018f63b0516560823519017-640-0.webp",
        "image_secondary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/edit-23-06-41-e8e01b292e18469cba16560823522994-640-0.webp",
        "type":"sofas"
      },
      {
        "id":34,
        "name":"MADRID",
        "description":"EL VALOR PUBLICADO CORRESPONDE A LA MEDIDA DE 2.00x090 Consultanos su valor en otras medidas: 1.80/ 2.20 / formato esquinero ¿Que opciones&nbsp;incluyen los preci...",
        "price":"890900",
        "cash_price":"712720",
        "image_primary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/edit-21-07_11-bba945fe521af92a3f16588541148652-640-0.webp",
        "image_secondary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/edit-21-07_21-c443e0c5e82446e2af16588541150227-640-0.webp",
        "type":"sofas"
      },
      {
        "id":35,
        "name":"BERLIN",
        "description":"EL VALOR PUBLICADO CORRESPONDE A LA MEDIDA DE 200x090 *Adicionales en la foto no incluidos en el valor: Tapizado Panne antimanchas Consultanos su valor en ot...",
        "price":"612700",
        "cash_price":"490160",
        "image_primary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/edit-21-4fb738cfef131f22b816564400900176-640-0.webp",
        "image_secondary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/edit-31-33e6ccd5fd3dc83c2016564400898399-640-0.webp",
        "type":"sofas"
      },
      {
        "id":36,
        "name":"VENECIA",
        "description":"EL VALOR PUBLICADO CORRESPONDE A LA MEDIDA DE 200x090 Consultanos su valor en otras medidas: 1.40 / 1.50 / 1.60 / 1.80 / 1.90&nbsp;/ 2.20 / 2.30 / 2.50 / formato ...",
        "price":"612700",
        "cash_price":"490160",
        "image_primary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/edit-05-07_131-6ee5b49400344f6aad16572157382034-640-0.webp",
        "image_secondary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/edit-05-07_151-9f592ca193f1f9abba16572157384971-640-0.webp",
        "type":"sofas"
      },
      {
        "id":37,
        "name":"BALI",
        "description":"EL VALOR PUBLICADO CORRESPONDE A LA MEDIDA DE 1.80x090 Consultanos su valor en otras medidas: 2.00 / 2.20 / formato esquinero ¿Que opciones&nbsp;incluyen los prec...",
        "price":"828000",
        "cash_price":"662400",
        "image_primary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/edit-05-07_71-bfab1209ebf0ae0e7716572162223080-640-0.webp",
        "image_secondary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/edit-05-07_61-951d95e89b4439cf5516572162225767-640-0.webp",
        "type":"sofas"
      },
      {
        "id":38,
        "name":"ITALIANO",
        "description":"EL VALOR PUBLICADO CORRESPONDE A LA MEDIDA DE 1.80X0.90 *Adicionales en la foto no incluidos en el valor: Mojito antimanchas Consultanos su valor en otras me...",
        "price":"572200",
        "cash_price":"457760",
        "image_primary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/edit-07-09_36-a4a536c7ebc9da44f616628728640126-640-0.webp",
        "image_secondary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/edit-07-09_371-94d9936a0f0ce21e9116626508928486-640-0.webp",
        "type":"sofas"
      },
      {
        "id":39,
        "name":"MADISON",
        "description":"EL VALOR PUBLICADO CORRESPONDE A LA MEDIDA DE 1.80X0.90 *Adicionales en la foto no incluidos en el valor: Mojito antimanchas / vellon en asiento Consultanos ...",
        "price":"572200",
        "cash_price":"457760",
        "image_primary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/edit-25-08_46-11-bad999c9ea8670b35216667112503687-640-0.webp",
        "image_secondary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/edit-25-08_471-47498edb94506201b716667112504709-640-0.webp",
        "type":"sofas"
      },
      {
        "id":40,
        "name":"LISBOA",
        "description":"EL VALOR PUBLICADO CORRESPONDE A LA MEDIDA DE 160x090 *Adicionales en la foto no incluidos en el valor: Tapizado Mojito Consultanos su valor en otras medid...",
        "price":"541100",
        "cash_price":"432880",
        "image_primary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/edit-02-08_11-1cec2ad5abdbd2e99a16603352948670-640-0.webp",
        "image_secondary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/edit-02-08_01-8319f2ab0994c024c116603352946602-640-0.webp",
        "type":"sofas"
      },
      {
        "id":41,
        "name":"MYKONOS",
        "description":"EL VALOR PUBLICADO CORRESPONDE A LA MEDIDA DE 2.00x0.90 Consultanos su valor en otras medidas: 1.80x0.90&nbsp;/ 2.20x0.90 / 2.20x0.90 ¿Que opciones&nbsp;incluyen los p...",
        "price":"660700",
        "cash_price":"528560",
        "image_primary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/whatsapp-image-2023-03-09-at-11-23-381-8e52ecb2d05fae3f9416783719477676-640-0.webp",
        "image_secondary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/whatsapp-image-2023-03-09-at-11-23-391-b0ebe945e60ad1529516783719479086-640-0.webp",
        "type":"sofas"
      },
      {
        "id":42,
        "name":"MONTREAL",
        "description":"EL VALOR PUBLICADO CORRESPONDE A LA MEDIDA DE 2.20x1.10 *Adicionales en la foto no incluidos en el valor: Tapizado Mojito antimanchas Consultanos su valor ...",
        "price":"1150700",
        "cash_price":"920560",
        "image_primary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/image-11-1195358abedb2c79bb16806287543641-640-0.webp",
        "image_secondary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/image21-dbcc9a0e78db79c21816806287543859-640-0.webp",
        "type":"sofas"
      },
      {
        "id":43,
        "name":"PERSIA",
        "description":"EL VALOR PUBLICADO CORRESPONDE A LA MEDIDA DE 1.80x090 Consultanos su valor en otras medidas: 2.00 / 2.20 / formato esquinero ¿Que opciones&nbsp;incluyen los prec...",
        "price":"910800",
        "cash_price":"728640",
        "image_primary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/image-31-3c565e4fc7c1fc472a16855429645624-640-0.webp",
        "image_secondary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/image-11-737ba808f15a0aea5d16855429646235-640-0.webp",
        "type":"sofas"
      },
      {
        "id":44,
        "name":"DECO LISO",
        "description":"Los decos miden 50x50 estan tapizados en pana&nbsp;y&nbsp;rellenos de puro vellón. Elegi tu color favorito! son un producto&nbsp;fundamental para tu decoracion.",
        "price":"15700",
        "cash_price":"",
        "image_primary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/dsc_0512a-c8c2d51ca770dc113417083541274029-640-0.webp",
        "image_secondary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/dsc_0512a-c8c2d51ca770dc113417083541274029-640-0.webp",
        "type":"complemento"
      },
      {
        "id":45,
        "name":"RESPALDO VAINILLA",
        "description":"EL PRODUCTO DE LA IMAGEN ESTÁ PRESUPUESTADO&nbsp;EN LA MEDIDA DE:&nbsp;1.60x1.30 CONSULTA SU VALOR EN LAS MEDIDAS DE: 1.40 o 2.00 metros Tapizado:&nbsp;pana antimanchas / c...",
        "price":"189800",
        "cash_price":"151840",
        "image_primary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/respaldo-5c889a2d5da87b0f3017000601620437-640-0.webp",
        "image_secondary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/respaldo-5c889a2d5da87b0f3017000601620437-640-0.webp",
        "type":"complemento"
      },
      {
        "id":46,
        "name":"RESPALDO",
        "description":"EL PRODUCTO DE LA IMAGEN ESTÁ PRESUPUESTADO&nbsp;EN LA MEDIDA DE:&nbsp;1.60x1.30 CONSULTA SU VALOR EN LAS MEDIDAS DE: 1.40 o 2.00 metros Tapizado:&nbsp;pana antimanchas / c...",
        "price":"166700",
        "cash_price":"133360",
        "image_primary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/whatsapp-image-2023-01-23-at-1-03-50-pm-21-26a082be71f6eb3a9416744899107351-640-0.webp",
        "image_secondary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/whatsapp-image-2023-01-23-at-1-03-50-pm1-4137b55cb207e3916216744899108017-640-0.webp",
        "type":"complemento"
      },
      {
        "id":47,
        "name":"MANTA",
        "description":"Manta confeccionada 100% algodón. Medida 1.50x1.40 ¡Consultanos por más colores!",
        "price":"20500",
        "cash_price":"16400",
        "image_primary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/edit-26-10_11-1db792c092efc4a8b616672291678960-640-0.webp",
        "image_secondary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/edit-26-10_21-26972e6aa0aaf201db16672291677047-640-0.webp",
        "type":"complemento"
      },
      {
        "id":48,
        "name":"VINTAGE",
        "description":"EL VALOR PUBLICADO CORRESPONDE A LA MEDIDA DE 2.00x1.60 Consultanos su valor en otras medidas: 1.80x1.60 / 2.20x1.60 / 2.30x1.80 / 2.50x1.80 / 2.80x2.00 ¿Que...",
        "price":"765200",
        "cash_price":"612160",
        "image_primary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/edit-28-06_91-dfec36456850050df216606641698092-640-0.webp",
        "image_secondary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/edit-28-06_101-6152da097b41b1f70916606641699873-640-0.webp",
        "type":"esquineros"
      },
      {
        "id":49,
        "name":"LOS ANGELES",
        "description":"EL VALOR PUBLICADO CORRESPONDE A LA MEDIDA DE 2.50x1.70 Consultanos su valor en otras medidas: 2.00x1.70 / 2.20x1.70&nbsp; ¿Que opciones&nbsp;incluyen los precios base...",
        "price":"1038100",
        "cash_price":"830480",
        "image_primary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/edit-01-05-23_54-9c1686fd565885064717080828740600-640-0.webp",
        "image_secondary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/edit-01-05-23_55-a114021a38886f8c0f17080828769961-640-0.webp",
        "type":"esquineros"
      },
      {
        "id":50,
        "name":"DALI",
        "description":"EL VALOR PUBLICADO CORRESPONDE A LA MEDIDA DE 2.20x1.60 *Adicionales en la foto no incluidos en el valor: Base de madera / Panne antimanchas&nbsp; Consultanos su ...",
        "price":"833700",
        "cash_price":"666960",
        "image_primary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/edit-02-08_151-7143ba325e7c16fdce16595282304498-640-0.webp",
        "image_secondary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/edit-02-08_161-60d28988007433254616595282305959-640-0.webp",
        "type":"esquineros"
      },
      {
        "id":51,
        "name":"CAROL",
        "description":"EL VALOR PUBLICADO CORRESPONDE A LA MEDIDA DE 1.80x1.60 Consultanos su valor en otras medidas: 2.00x1.60 / 2.20x1.60 / 2.30x1.80 / 2.50x1.80 / 2.80x2.00 ¿Que...",
        "price":"710700",
        "cash_price":"568560",
        "image_primary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/edit-25-08_171-e7e70ec0eae728d41516618744430433-640-0.webp",
        "image_secondary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/edit-25-08_181-b12563396501fcbe9516618744433511-640-0.webp",
        "type":"esquineros"
      },
      {
        "id":52,
        "name":"CHICAGO",
        "description":"EL VALOR PUBLICADO CORRESPONDE A LA MEDIDA DE 2.00x1.60 *Adicionales en la foto no incluidos en el valor: Base de madera Consultanos su valor en otras medida...",
        "price":"742900",
        "cash_price":"594320",
        "image_primary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/edit-05-07_281-9552d164c62862be0e16588572785614-640-0.webp",
        "image_secondary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/edit-05-07_291-365e3b4ffaef04102016588572788189-640-0.webp",
        "type":"esquineros"
      },
      {
        "id":53,
        "name":"VICTORIA",
        "description":"EL VALOR PUBLICADO CORRESPONDE A LA MEDIDA DE 2.00x1.60 Consultanos su valor en otras medidas: 1.80x1.60 / 2.20x1.60 / 2.30x1.80 / 2.50x1.80 / 2.80x2.00 ¿Que...",
        "price":"742900",
        "cash_price":"594320",
        "image_primary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/edit-28-06_3611-05029a8eb1e4f4292c16606640770639-640-0.webp",
        "image_secondary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/edit-28-06_351-288d10216ac6698fab16606640771372-640-0.webp",
        "type":"esquineros"
      },
      {
        "id":54,
        "name":"TOKIO",
        "description":"EL VALOR PUBLICADO CORRESPONDE A LA MEDIDA DE 2.00x1.60 *Adicionales en la foto no incluidos en el valor: Tapizado mojito antimanchas Consultanos su valor en...",
        "price":"742900",
        "cash_price":"594320",
        "image_primary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/edit-28-06_441-6fa8fa972750d2226f16606644721315-640-0.webp",
        "image_secondary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/edit-28-06_4311-4665ff80d1ca8c7da416606644722189-640-0.webp",
        "type":"esquineros"
      },
      {
        "id":55,
        "name":"BUENOS AIRES",
        "description":"EL VALOR PUBLICADO CORRESPONDE A LA MEDIDA DE 2.00x1.60 *Adicionales en la foto no incluidos en el valor: Mojito antimanchas / Vellón en asiento Consultanos ...",
        "price":"742900",
        "cash_price":"594320",
        "image_primary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/edit-28-06_191-7e965c5e6ac1f6818116564447256960-640-0.webp",
        "image_secondary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/edit-28-06_231-a3c71eae3b5f7bf4b816564447258924-640-0.webp",
        "type":"esquineros"
      },
      {
        "id":56,
        "name":"BERLIN",
        "description":"EL VALOR PUBLICADO CORRESPONDE A LA MEDIDA DE 2.30x1.80 *Adicionales en la foto no incluidos en el valor: Base de madera Consultanos su valor en otras medida...",
        "price":"832900",
        "cash_price":"666320",
        "image_primary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/edit-25-08_771-42da27981bb74849b616618745769176-640-0.webp",
        "image_secondary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/edit-25-08_781-cf20e2c80a32051e6016618745768543-640-0.webp",
        "type":"esquineros"
      },
      {
        "id":57,
        "name":"PRAGA",
        "description":"EL VALOR PUBLICADO CORRESPONDE A LA MEDIDA DE 2.30x1.80 *Adicionales en la foto no incluidos en el valor: Panne antimanchas Consultanos su valor en otras med...",
        "price":"832900",
        "cash_price":"666320",
        "image_primary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/edit-05-07_361-91c2fad162ec2e87f116572150942151-640-0.webp ",
        "image_secondary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/edit-05-07_351-ed2486d028b33ed31516572150942876-640-0.webp",
        "type":"esquineros"
      },
      {
        "id":58,
        "name":"ATHENAS",
        "description":"EL VALOR PUBLICADO CORRESPONDE A LA MEDIDA DE 2.00x1.60 *Adicionales en la foto no incluidos en el valor: Base de madera Consultanos su valor en otras medida...",
        "price":"742900",
        "cash_price":"594320",
        "image_primary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/edit-28-06_301-3cc3949307644e172316564413955225-640-0.webp",
        "image_secondary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/edit-28-06_321-54c27780eaed9565f816564413912111-640-0.webp",
        "type":"esquineros"
      },
      {
        "id":59,
        "name":"VENECIA",
        "description":"EL VALOR PUBLICADO CORRESPONDE A LA MEDIDA DE 2.00x1.60 Consultanos su valor en otras medidas: 1.80x1.60 / 2.20x1.60 / 2.30x1.80 / 2.50x1.80 / 2.80x2.00 ¿Que...",
        "price":"742900",
        "cash_price":"594320",
        "image_primary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/edit-28-06_181-22b2e5c42361f8bf1716606639902171-640-0.webp",
        "image_secondary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/edit-28-06_191-c16dc7245cbf8b605916606639894963-640-0.webp",
        "type":"esquineros"
      },
      {
        "id":60,
        "name":"DUBLÍN",
        "description":"EL VALOR PUBLICADO CORRESPONDE A LA MEDIDA DE 2.20x1.60 Consultanos su valor en otras medidas: 1.80x1.60 / 2.00x1.60 / 2.30x1.80 / 2.50x1.80 / 2.80x2.00 ¿Que...",
        "price":"793900",
        "cash_price":"635120",
        "image_primary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/edit-21-07_151-dc6bcdd489d7abfef216588546822373-640-0.webp",
        "image_secondary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/edit-21-07_161-de593cf0f99617c1f716588546825508-640-0.webp",
        "type":"esquineros"
      },
      {
        "id":61,
        "name":"VERONA",
        "description":"EL VALOR PUBLICADO CORRESPONDE A LA MEDIDA DE 2.00x1.60 *Adicionales en la foto no incluidos en el valor: Base de madera&nbsp; Consultanos su valor en otras medid...",
        "price":"742900",
        "cash_price":"594320",
        "image_primary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/edit-23-06-321-df54ab5a3d4fe3d55f16564440104933-640-0.webp",
        "image_secondary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/edit-23-06-361-8916ca7549be5cbe7e16564440101697-640-0.webp",
        "type":"esquineros"
      },
      {
        "id":62,
        "name":"LUXURY",
        "description":"EL VALOR PUBLICADO CORRESPONDE A LA MEDIDA DE 2.20x1.70 Consultanos su valor en otras medidas: 2.00x1.70 / 2.50x1.70&nbsp; ¿Que opciones&nbsp;incluyen los precios base...",
        "price":"910000",
        "cash_price":"728000",
        "image_primary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/image-51-50604bd55800d0ae2816806286347068-640-0.webp",
        "image_secondary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/image-31-829510aaf1402e671316806286348802-640-0.webp",
        "type":"esquineros"
      },
      {
        "id":63,
        "name":"LONDON",
        "description":"EL VALOR PUBLICADO CORRESPONDE A LA MEDIDA DE 2.20x1.60 *Adicionales en la foto no incluidos en el valor: Vivos Consultanos su valor en otras medidas: 1.80x1...",
        "price":"793900",
        "cash_price":"635120",
        "image_primary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/image-21-0542fbfd1bd70593a216806285958028-640-0.webp",
        "image_secondary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/image-41-0d8ae70d0771bc43a116806285957293-640-0.webp",
        "type":"esquineros"
      },
      {
        "id":64,
        "name":"PARIS",
        "description":"EL VALOR PUBLICADO CORRESPONDE A LA MEDIDA DE 1.80x1.60 Consultanos su valor en otras medidas: 2.00x1.60 / 2.20x1.60 / 2.30x1.80 / 2.50x1.80 / 2.80x2.00 ¿Que...",
        "price":"710700",
        "cash_price":"568560",
        "image_primary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/edit-07-09_23-1a3cf2cc74bcb8e3a716628983628682-640-0.webp",
        "image_secondary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/edit-07-09_241-4a481a10b873fe312116626515668575-640-0.webp",
        "type":"esquineros"
      },
      {
        "id":65,
        "name":"SEATTLE",
        "description":"EL VALOR PUBLICADO CORRESPONDE A LA MEDIDA DE 1.80x1.60 Consultanos su valor en otras medidas: 2.00x1.60 / 2.20x1.60 / 2.30x1.80 / 2.50x1.80 / 2.80x2.00 ¿Que...",
        "price":"717000",
        "cash_price":"573600",
        "image_primary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/seattle-11-d25028923adc08358a16643788069791-640-0.webp",
        "image_secondary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/seattle1-e6d780828b8285e20f16643788071011-640-0.webp",
        "type":"esquineros"
      },
      {
        "id":66,
        "name":"BRAMPTON",
        "description":"EL VALOR PUBLICADO CORRESPONDE A LA MEDIDA DE 2.00x1.70 *Adicionales en la foto no incluidos en el valor: Mojito antimanchas Consultanos su valor en otras me...",
        "price":"878100",
        "cash_price":"702480",
        "image_primary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/edit-01-05-23_46-2457c0177628716f6917080831260214-640-0.webp",
        "image_secondary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/edit-01-05-23_46-2457c0177628716f6917080831260214-640-0.webp",
        "type":"esquineros"
      },
      {
        "id":67,
        "name":"LISBOA",
        "description":"EL VALOR PUBLICADO CORRESPONDE A LA MEDIDA DE 2.00x1.60 Consultanos su valor en otras medidas: 1.80x1.60 / 2.20x1.60 / 2.30x1.80 / 2.50x1.80 / 2.80x2.00 ¿Que...",
        "price":"742900",
        "cash_price":"594320",
        "image_primary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/edit-01-05-23_6211-0c1f2a31dc53ad131316831201710546-640-0.webp",
        "image_secondary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/edit-01-05-23_6311-3a08cf8d1e5f3b56fe16831201711366-640-0.webp",
        "type":"esquineros"
      },
      {
        "id":68,
        "name":"MANHATTAN",
        "description":"EL VALOR PUBLICADO CORRESPONDE A LA MEDIDA DE 2.00x1.60 Consultanos su valor en otras medidas: 1.80x1.60 / 2.20x1.60 / 2.30x1.80 / 2.50x1.80 / 2.80x2.00 ¿Que...",
        "price":"765200",
        "cash_price":"612160",
        "image_primary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/image-41-1f708569a4d31c381a16855428231594-640-0.webp",
        "image_secondary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/image-51-df648ddd8313e1482a16855428236031-640-0.webp",
        "type":"esquineros"
      },
      {
        "id":69,
        "name":"MISSOURI",
        "description":"EL VALOR PUBLICADO CORRESPONDE A LA MEDIDA DE 2.00x1.60 Consultanos su valor en otras medidas: 1.80x1.60 / 2.20x1.60 / 2.30x1.80 / 2.50x1.80 / 2.80x2.00 ¿Que...",
        "price":"742900",
        "cash_price":"594320",
        "image_primary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/edit-07-09_8-8298bdfb38d4f1159517080829547736-640-0.webp",
        "image_secondary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/edit-07-09_9-69e182e4e2d669e0f817080829572510-640-0.webp",
        "type":"esquineros"
      },
      {
        "id":70,
        "name":"MADISON",
        "description":"EL VALOR PUBLICADO CORRESPONDE A LA MEDIDA DE 2.00x1.60 Consultanos su valor en otras medidas: 1.80x1.60 / 2.20x1.60 / 2.30x1.80 / 2.50x1.80 / 2.80x2.00 ¿Que...",
        "price":"742900",
        "cash_price":"594320",
        "image_primary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/edit-13-07_22-a1d766d038c282cb0e17080831104164-640-0.webp",
        "image_secondary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/edit-13-07_23-0339ca41047c40047117080831146550-640-0.webp",
        "type":"esquineros"
      },
      {
        "id":71,
        "name":"MOSCU",
        "description":"EL VALOR PUBLICADO CORRESPONDE A LA MEDIDA DE 2.20x1.60 Consultanos su valor en otras medidas: 1.80x1.60 / 2.00x1.60 / 2.30x1.80 / 2.50x1.80 / 2.80x2.00 ¿Que...",
        "price":"793900",
        "cash_price":"635120",
        "image_primary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/edit-12-06-23_56-d03c8a776e0faeee0617081134543833-640-0.webp",
        "image_secondary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/edit-12-06-23_57-11564b12531e99dd7117081134566099-640-0.webp",
        "type":"esquineros"
      },
      {
        "id":72,
        "name":"MADRID",
        "description":"EL VALOR PUBLICADO CORRESPONDE A LA MEDIDA DE 2.00x1.60 Consultanos su valor en otras medidas: 2.20x1.60 / 2.50x1.80&nbsp; ¿Que opciones&nbsp;incluyen los precios base...",
        "price":"1063000",
        "cash_price":"850400",
        "image_primary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/edit-25-03-2023_18-d4740f1dfef39a062717081136515637-640-0.webp",
        "image_secondary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/edit-25-03-2023_19-a96fdd1bbcb8ee220a17081136540023-640-0.webp",
        "type":"esquineros"
      },
      {
        "id":73,
        "name":"SEATTLE",
        "description":"EL VALOR PUBLICADO CORRESPONDE A LA MEDIDA DE 2.50x1.85 *Adicionales en la foto no incluidos en el valor: Panne antimanchas Consultanos su valor en otras m...",
        "price":"1067700",
        "cash_price":"854160",
        "image_primary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/edit-20-10_12_edit-31-4a85598d3a3709d7c716730194084778-640-0.webp",
        "image_secondary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/edit-20-10_12_edit-21-4a85598d3a3709d7c716730194086870-640-0.webp",
        "type":"rinconeros"
      },
      {
        "id":74,
        "name":"NAPOLES",
        "description":"EL VALOR PUBLICADO CORRESPONDE A LA MEDIDA DE 2.40x200 *Adicionales en la foto no incluidos en el valor: Panne antimanchas Consultanos su valor en otras medi...",
        "price":"1024200",
        "cash_price":"819360",
        "image_primary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/dsc_0926-2eba52404700764f5617081133706360-640-0.webp",
        "image_secondary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/dsc_0926-2eba52404700764f5617081133706360-640-0.webp",
        "type":"rinconeros"
      },
      {
        "id":75,
        "name":"RINCONERO BUENOS AIRES",
        "description":"EL VALOR PUBLICADO CORRESPONDE A LA MEDIDA DE 2.50x1.80 Consultanos su valor en otras medidas: 2.80x2.20 / 3.10x2.40 ¿Que opciones&nbsp;incluyen los precios base?...",
        "price":"1047300",
        "cash_price":"837840",
        "image_primary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/edit-20-10_111-2202eb7b20382d289416666285391941-640-0.webp",
        "image_secondary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/edit-20-10_211-8cc9d359cc828c9cab16666285394958-640-0.webp",
        "type":"rinconeros"
      },
      {
        "id":76,
        "name":"DALI",
        "description":"EL VALOR PUBLICADO CORRESPONDE A LA MEDIDA DE 2.50x1.80 Consultanos su valor en otras medidas: 2.80x2.20 / 3.10x2.40 ¿Que opciones&nbsp;incluyen los precios base?...",
        "price":"1087100",
        "cash_price":"869680",
        "image_primary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/edit-22-12_1051-be0f8dbbd82810304316730199587572-640-0.webp",
        "image_secondary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/edit-22-12_1111-2f82742b3a393f0ad116730199588667-640-0.webp",
        "type":"rinconeros"
      },
      {
        "id":77,
        "name":"DUBLIN",
        "description":"EL VALOR PUBLICADO CORRESPONDE A LA MEDIDA DE 2.50x1.80 Consultanos su valor en otras medidas: 2.80x2.20 / 3.10x2.40 ¿Que opciones&nbsp;incluyen los precios bas...",
        "price":"1047300",
        "cash_price":"837840",
        "image_primary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/edit-22-12_871-e0aba311c287aa8e1616730196349934-640-0.webp",
        "image_secondary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/edit-22-12_941-b537327a35b02e2e3d16730196349116-640-0.webp",
        "type":"rinconeros"
      },
      {
        "id":78,
        "name":"ATHENAS",
        "description":"EL VALOR PUBLICADO CORRESPONDE A LA MEDIDA DE 2.50x1.80 Consultanos su valor en otras medidas: 2.80x2.20 / 3.10x2.40 ¿Que opciones&nbsp;incluyen los precios bas...",
        "price":"1047300",
        "cash_price":"837840",
        "image_primary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/copia-de-dsc_0171a-807b81a6c4edbe11f917081133421099-640-0.webp",
        "image_secondary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/copia-de-dsc_0171a-807b81a6c4edbe11f917081133421099-640-0.webp",
        "type":"rinconeros"
      },
      {
        "id":79,
        "name":"DIVAN CAMA",
        "description":"EL VALOR PUBLICADO CORRESPONDE A LA MEDIDA DE 2.10x0.90 / el mismo viene con el colchon incluido.&nbsp; Consultanos su valor en otras medidas: 2.20 / 2.30 ¿Que op...",
        "price":"874500",
        "cash_price":"699600",
        "image_primary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/edit-13-07_301-e5fec9ca111e796e7016588550812569-640-0.webp",
        "image_secondary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/edit-13-07_3711-ef21359b14c5ec312516596389357881-640-0.webp",
        "type":"sofa-cama"
      },
      {
        "id":80,
        "name":"SOFA CAMA DALI",
        "description":"EL VALOR PUBLICADO CORRESPONDE A LA MEDIDA DE 1.75X0.90 (2 PLAZAS) Consultanos su valor en otras medidas: 1 plaza / 1 plaza y media ¿Que opciones&nbsp;incluyen lo...",
        "price":"1231500",
        "cash_price":"985200",
        "image_primary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/sofa-cama-11-0d6c88bd17411018a016643792910116-640-0.webp",
        "image_secondary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/sofa-cama1-7fa524caaa3514771316643792911590-640-0.webp",
        "type":"sofa-cama"
      },
      {
        "id":81,
        "name":"DIVAN CAMA DALI",
        "description":"EL VALOR PUBLICADO CORRESPONDE A LA MEDIDA DE 2.10x0.90 / el mismo viene con el colchon incluido.&nbsp; Consultanos su valor en otras medidas: 2.20 / 2.30 ¿Que op...",
        "price":"914300",
        "cash_price":"731440",
        "image_primary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/divan-cama-da1a841eddb860d37817148351700922-640-0.webp",
        "image_secondary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/divan-cama-da1a841eddb860d37817148351700922-640-0.webp",
        "type":"sofa-cama"
      },
      {
        "id":82,
        "name":"Esquinero Verona / Precio especial 2x1.60",
        "description":"¿CÓMO FUNCIONA ESTA PROMO? *El valor expresado en esta publicación es por la medida de 2.00x1.60 Únicamente tapizado CITY antidesgarro (tapizado de la foto...",
        "price":"697400",
        "cash_price":"557920",
        "image_primary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/image-51-73aacc94cebc9c108516787922032589-640-0.webp",
        "image_secondary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/edit-31-01-23_2-11-36c992f4576f3dbefa16764975179012-640-0.webp",
        "type":"precio-especial"
      },
      {
        "id":83,
        "name":"Verona / Precio especial 1.80",
        "description":"¿CÓMO FUNCIONA ESTA PROMO? *El valor expresado en esta publicación es por la medida de 180x090 Únicamente tapizado CITY antidesgarro (tapizado de la foto c...",
        "price":"536400",
        "cash_price":"429120",
        "image_primary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/image-61-a128c8d7c13167be8716787921899773-640-0.webp",
        "image_secondary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/edit-30-01-23_91-ca400ada222a5711cb16764972758860-640-0.webp",
        "type":"precio-especial"
      },
      {
        "id":84,
        "name":"Esquinero Verona / Precio especial 1.80x1.60",
        "description":"¿CÓMO FUNCIONA ESTA PROMO? *El valor expresado en esta publicación es por la medida de 1.80x1.60 Únicamente tapizado CITY antidesgarro (tapizado de la foto...",
        "price":"668300",
        "cash_price":"534640",
        "image_primary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/image-51-c513781b19c521b93d17083552351802-640-0.jpeg",
        "image_secondary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/edit-31-01-23_2-11-654ba9fb4954e6977117083552398326-640-0.jpg",
        "type":"precio-especial"
      },
      {
        "id":85,
        "name":"Esquinero Verona / Precio especial 2.20x1.60",
        "description":"¿CÓMO FUNCIONA ESTA PROMO? *El valor expresado en esta publicación es por la medida de 2.20x1.60 Únicamente tapizado CITY antidesgarro (tapizado de la foto...",
        "price":"741800",
        "cash_price":"593440",
        "image_primary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/image-51-1714c4e05669438e1d17083551897640-640-0.jpeg",
        "image_secondary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/edit-31-01-23_2-11-15ac985fa8adc6248717083551943625-640-0.jpg",
        "type":"precio-especial"
      },
      {
        "id":86,
        "name":"Verona / Precio especial 2",
        "description":"¿CÓMO FUNCIONA ESTA PROMO? *El valor expresado en esta publicación es por la medida de 200x090 Únicamente tapizado CITY antidesgarro (tapizado de la foto cor...",
        "price":"573600",
        "cash_price":"458880",
        "image_primary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/image-61-4aeba15956d10d69f217083550671432-640-0.jpeg",
        "image_secondary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/edit-30-01-23_91-1719fe9bbe9d46a7bc17083550726035-640-0.jpg",
        "type":"precio-especial"
      },
      {
        "id":87,
        "name":"Verona / Precio especial 1.60",
        "description":"¿CÓMO FUNCIONA ESTA PROMO? *El valor expresado en esta publicación es por la medida de 160x090 Únicamente tapizado CITY antidesgarro (tapizado de la foto cor...",
        "price":"508600",
        "cash_price":"406880",
        "image_primary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/image-61-d012b2aefb4adc3d7f17083549178854-640-0.jpeg",
        "image_secondary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/edit-30-01-23_91-17f7c12a922ca3120a17083549224240-640-0.jpg",
        "type":"precio-especial"
      },
      {
        "id":88,
        "name":"PUFF CUADRADO",
        "description":"EL PRODUCTO DE LA IMAGEN TIENE UNA MEDIDA UNICA ¿Que opciones&nbsp;incluyen los precios base? Telas:&nbsp;pana antimanchas / chenille antidesgarro / lino antimanchas P...",
        "price":"68500",
        "cash_price":"54800",
        "image_primary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/puf-cuadrado1-9206360987adc58f5e16745806131296-640-0.webp",
        "image_secondary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/puf-cuadrado1-9206360987adc58f5e16745806131296-640-0.webp",
        "type":"individuales"
      },
      {
        "id":89,
        "name":"POLTRONA",
        "description":"EL PRODUCTO DE LA IMAGEN TIENE UNA MEDIDA UNICA *Adicionales en la foto no incluidos en el valor: Tapizado Mojito antimanchas ¿Que opciones&nbsp;incluyen los prec...",
        "price":"295900",
        "cash_price":"236720",
        "image_primary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/poltrona-11-b4fd045cfd0d67d65616643785645542-640-0.webp",
        "image_secondary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/poltrona1-a8d84d3161ab12286816643785644024-640-0.webp",
        "type":"individuales"
      },
      {
        "id":90,
        "name":"MIAMI",
        "description":"EL PRODUCTO DE LA IMAGEN TIENE UNA MEDIDA UNICA *Adicionales en la foto no incluidos en el valor: Tapizado Mojito antimanchas ¿Que opciones&nbsp;incluyen los prec...",
        "price":"231300",
        "cash_price":"185040",
        "image_primary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/edit-20-10_211-2c397e3ed81738ce6616744896985260-640-0.webp",
        "image_secondary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/edit-20-10_201-e52d2a3f504423d60616744896986160-640-0.webp",
        "type":"individuales"
      },
      {
        "id":91,
        "name":"PUFF REDONDO",
        "description":"EL PRODUCTO DE LA IMAGEN TIENE UNA MEDIDA UNICA ¿Que opciones&nbsp;incluyen los precios base? Telas:&nbsp;pana antimanchas / chenille antidesgarro / lino antimanchas P...",
        "price":"98100",
        "cash_price":"78480",
        "image_primary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/puf-redondo1-a24bdd9b6277625aaf16745804998497-640-0.webp",
        "image_secondary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/puf-redondo1-a24bdd9b6277625aaf16745804998497-640-0.webp",
        "type":"individuales"
      },
      {
        "id":92,
        "name":"PUFF EXAGONAL",
        "description":"EL PRODUCTO DE LA IMAGEN TIENE UNA MEDIDA UNICA ¿Que opciones&nbsp;incluyen los precios base? Telas:&nbsp;pana antimanchas / chenille antidesgarro / lino antimanchas P...",
        "price":"112400",
        "cash_price":"89920",
        "image_primary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/dsc_0692a-000531e15898cee2f117080253251684-640-0.webp",
        "image_secondary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/dsc_0692a-000531e15898cee2f117080253251684-640-0.webp",
        "type":"individuales"
      },
      {
        "id":93,
        "name":"MONACO",
        "description":"EL PRODUCTO DE LA IMAGEN TIENE UNA MEDIDA UNICA *Adicionales en la foto no incluidos en el valor: Tapizado Mojito antimanchas ¿Que opciones&nbsp;incluyen los prec...",
        "price":"567800",
        "cash_price":"454240",
        "image_primary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/edit-11-04-231-5f4f6d9046ebeeeb2d16812345752654-640-0.webp",
        "image_secondary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/whatsapp-image-2023-04-11-at-2-34-56-pm1-f2704bdabd7bc5436d16812345722464-640-0.webp",
        "type":"individuales"
      },
      {
        "id":94,
        "name":"TOULOUSE",
        "description":"EL PRODUCTO DE LA IMAGEN TIENE UNA MEDIDA UNICA ¿Que opciones&nbsp;incluyen los precios base? Telas:&nbsp;pana antimanchas / chenille antidesgarro / lino antimanchas P...",
        "price":"256900",
        "cash_price":"205520",
        "image_primary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/edit-31-01-23_391-e0eed4fff5605151fd16756823751377-640-0.webp",
        "image_secondary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/edit-31-01-23_391-e0eed4fff5605151fd16756823751377-640-0.webp",
        "type":"individuales"
      },
      {
        "id":95,
        "name":"BERGER",
        "description":"EL PRODUCTO DE LA IMAGEN TIENE UNA MEDIDA UNICA *Adicionales en la foto no incluidos en el valor: Tapizado Mojito antimanchas ¿Que opciones&nbsp;incluyen los prec...",
        "price":"491700",
        "cash_price":"393360",
        "image_primary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/edit-31-01-23_351-3ed390a6082e48335a16756823663018-640-0.webp",
        "image_secondary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/edit-31-01-23_351-3ed390a6082e48335a16756823663018-640-0.webp",
        "type":"individuales"
      },
      {
        "id":96,
        "name":"Rack Memorial",
        "description":"Medida: 180x35cm Altura de 55cm Fabricado en enchapado paraiso de 19mm, terminacion en hidro laca semi mate Los estantes internos tienen una altura de 20cm e...",
        "price":"490700",
        "cash_price":"",
        "image_primary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/memorial-11-4ebf1705a7dfb8f71616559095076588-640-0.webp",
        "image_secondary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/memorial-21-2c87d8b83abda0ebe916559095066869-640-0.webp",
        "type":"muebles"
      },
      {
        "id":97,
        "name":"Mesa ratona Coliseo",
        "description":"Este juego esta compuesto por 2 mesas ratonas, una de 50cm de diametro y otra de 60cm de diametro. Fabricadas en mdf enchapado en paraiso de 18mm. Terminacio...",
        "price":"174300",
        "cash_price":"",
        "image_primary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/coliseo-11-21ab4e7c26c4bb6afa16559004017451-640-0.webp",
        "image_secondary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/coliseo-21-818389d791d221be4116559004018445-640-0.webp",
        "type":"muebles"
      },
      {
        "id":98,
        "name":"Rack York",
        "description":"Medida: 150x35cm Altura de 65cm Fabricada en madera enchapada de paraiso de 19mm, terminacion en hidro laca semi mate. Patas de hierro redondo de 2mm de diam...",
        "price":"425800",
        "cash_price":"",
        "image_primary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/rack-york-11-b7db2ba44caf57706a16559105699341-640-0.webp",
        "image_secondary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/rack-york-21-587c3ca005b59dc90316559105698800-640-0.webp",
        "type":"muebles"
      },
      {
        "id":99,
        "name":"Rack Met",
        "description":"Medida: 180x35cm Altura de 55cm Fabricado en enchapado paraiso de 19mm, terminacion en hidro laca semi mate. Tiene 2 puertas y 3 estantes.",
        "price":"490700",
        "cash_price":"",
        "image_primary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/met-11-09d5cbf40b5fa8918b16559097896898-640-0.webp",
        "image_secondary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/met-21-eefe736de910e273fc16559097896919-640-0.webp",
        "type":"muebles"
      },
      {
        "id":100,
        "name":"Perchero Everest",
        "description":"Medida: 55x10cm Altura de 190cm Fabricado en mdf de 15mm enchapado en paraiso con terminacion en&nbsp;hidro laca",
        "price":"89000",
        "cash_price":"",
        "image_primary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/everest-11-55ab6f4fb9793d9d3b16559010299124-640-0.webp",
        "image_secondary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/everest-21-69ae1bd4622ca35b7016559010302561-640-0.webp",
        "type":"muebles"
      },
      {
        "id":101,
        "name":"Perchero de pie Toronto",
        "description":"Medida: 1.80 de alto&nbsp; Ancho de 55cm",
        "price":"111100",
        "cash_price":"",
        "image_primary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/perchero-11-ec211af7b95ddaf71316842562099620-640-0.webp",
        "image_secondary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/perchero-21-9710cfe743718496bd16842562101638-640-0.webp",
        "type":"muebles"
      },
      {
        "id":102,
        "name":"Mesa ratona Osaka",
        "description":"Medida: 1.10x50 Altura de 42cm",
        "price":"231500",
        "cash_price":"",
        "image_primary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/image-11-60c9a8b6e7748d6daa16842560736870-640-0.webp",
        "image_secondary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/image1-14eaf9dcbcfffd099816842560736895-640-0.webp",
        "type":"muebles"
      },
      {
        "id":103,
        "name":"Mesa ratona Brooklyn",
        "description":"Medida: 1.10x55 Altura de 46cm",
        "price":"287100",
        "cash_price":"",
        "image_primary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/mesa-31-ad902ffc94b01e145716842558118783-640-0.webp",
        "image_secondary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/mesa-41-0c65f4906c691cb39d16842558122013-640-0.webp",
        "type":"muebles"
      },
      {
        "id":104,
        "name":"Mesa ratona Texas",
        "description":"Medida: 1.20x60 Altura de 46cm",
        "price":"226000",
        "cash_price":"",
        "image_primary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/mesa-51-acb174cf00bd9634e716842556221120-640-0.webp",
        "image_secondary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/mesa-61-ecbbcb226d419f8ce816842556220401-640-0.webp",
        "type":"muebles"
      },
      {
        "id":105,
        "name":"Mesa ratona Siena",
        "description":"Medida: 110x50cm Altura de 45cm Fabricada en paraiso macizo con tapa de mdf enchapado en paraiso de 18mm. Terminacion de hidro laca semi mate.",
        "price":"148200",
        "cash_price":"",
        "image_primary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/siena-11-9d9cf354cfbf00a1c316559075001669-640-0.webp",
        "image_secondary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/siena-31-73f700fa00009c22f716559074998078-640-0.webp",
        "type":"muebles"
      },
      {
        "id":106,
        "name":"MESA DE ARRIME HAWAII",
        "description":"Medida:&nbsp;35x35cm Altura de 65cm Fabricada en paraiso macizo, tapa en enchapado de paraiso de 18cm de espesor. Terminacion hidrolaca.",
        "price":"98200",
        "cash_price":"",
        "image_primary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/hawaii-11-7249b1ee6dbe7db2a016559007016150-640-0.webp",
        "image_secondary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/hawaii-31-1e6fa8e8575c9d4e2416559007021806-640-0.webp",
        "type":"muebles"
      },
      {
        "id":107,
        "name":"BIBLIOTECA BEN",
        "description":"Medida: 2 metros de altura x 75cm de ancho. La profundidad de los estantes es de 30cm. Fabricada en madera paraiso de 4x4cm y estantes de madera paraiso (enc...",
        "price":"268500",
        "cash_price":"",
        "image_primary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/ben-11-495d5bd94ab50c133416559001128200-640-0.webp",
        "image_secondary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/ben-21-26c5b7cfe8e9b0d70416559001129219-640-0.webp",
        "type":"muebles"
      },
      {
        "id":108,
        "name":"Mesa ratona Century",
        "description":"Medida: 1.10x0.50 Altura de 38cm Fabricada con mdf enchapado en guatambu de 19mm de espesor, con patas de guatambu macizo.",
        "price":"185200",
        "cash_price":"",
        "image_primary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/century-11-08a382b47bc4dd4ccd16558995988940-640-0.webp",
        "image_secondary":"https://dcdn.mitiendanube.com/stores/001/271/935/products/century-21-104b5381666dca830c16558995999681-640-0.webp",
        "type":"muebles"
      }
]

# Método para obtener todos los productos
@app.route('/', methods=['GET'])
def get_productos():
    lista_claves = ["sofas", "complemento", "esquineros", "rinconeros", "sofa-cama", "precio-especial", "individuales", "muebles"]
    lista_productos = []
    for clave in lista_claves:
      filtro = [p for p in productos if p["type"] == clave]
      lista_productos.append(filtro[0])
      lista_productos.append(filtro[1])
    print(len(lista_productos))
    return jsonify(lista_productos)

# Método para obtener un producto por ID
@app.route('/productos/<int:producto_id>', methods=['GET'])
def get_producto_by_id(producto_id):
    producto = next((p for p in productos if p["id"] == producto_id), None)
    if producto is not None:
        return jsonify(producto)
    else:
        return jsonify({"error": "Producto no encontrado"}), 404

# Método para obtener productos por tipo
@app.route('/sofas/', methods=['GET'])
def get_type_sofas():
    producto_type = "sofas"
    productos_filtrados = [p for p in productos if p["type"] == producto_type]
    if productos_filtrados:
        return jsonify(productos_filtrados)
    else:
        return jsonify({"error": "No se encontraron productos del tipo especificado"}), 404

# Método para obtener productos por tipo
@app.route('/complemento/', methods=['GET'])
def get_type_complemento():
    producto_type = "complemento"
    productos_filtrados = [p for p in productos if p["type"] == producto_type]
    if productos_filtrados:
        return jsonify(productos_filtrados)
    else:
        return jsonify({"error": "No se encontraron productos del tipo especificado"}), 404

# Método para obtener productos por tipo
@app.route('/esquineros/', methods=['GET'])
def get_type_esquineros():
    producto_type = "esquineros"
    productos_filtrados = [p for p in productos if p["type"] == producto_type]
    if productos_filtrados:
        return jsonify(productos_filtrados)
    else:
        return jsonify({"error": "No se encontraron productos del tipo especificado"}), 404


# Método para obtener productos por tipo
@app.route('/rinconeros/', methods=['GET'])
def get_type_rinconeros():
    producto_type = "rinconeros"
    productos_filtrados = [p for p in productos if p["type"] == producto_type]
    if productos_filtrados:
        return jsonify(productos_filtrados)
    else:
        return jsonify({"error": "No se encontraron productos del tipo especificado"}), 404

#sofa-cama
# Método para obtener productos por tipo
@app.route('/sofas-cama/', methods=['GET'])
def get_type_sofa_cama():
    producto_type = "sofa-cama"
    productos_filtrados = [p for p in productos if p["type"] == producto_type]
    if productos_filtrados:
        return jsonify(productos_filtrados)
    else:
        return jsonify({"error": "No se encontraron productos del tipo especificado"}), 404


# Método para obtener productos por tipo
@app.route('/precio-especial/', methods=['GET'])
def get_type_precio_especial():
    producto_type = "precio-especial"
    productos_filtrados = [p for p in productos if p["type"] == producto_type]
    if productos_filtrados:
        return jsonify(productos_filtrados)
    else:
        return jsonify({"error": "No se encontraron productos del tipo especificado"}), 404
    
# Método para obtener productos por tipo
@app.route('/individuales/', methods=['GET'])
def get_type_individuales():
    producto_type = "individuales"
    productos_filtrados = [p for p in productos if p["type"] == producto_type]
    if productos_filtrados:
        return jsonify(productos_filtrados)
    else:
        return jsonify({"error": "No se encontraron productos del tipo especificado"}), 404

# Método para obtener productos por tipo
@app.route('/muebles/', methods=['GET'])
def get_type_muebles():
    producto_type = "muebles"
    productos_filtrados = [p for p in productos if p["type"] == producto_type]
    if productos_filtrados:
        return jsonify(productos_filtrados)
    else:
        return jsonify({"error": "No se encontraron productos del tipo especificado"}), 404
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)