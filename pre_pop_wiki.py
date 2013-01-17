import pymongo
lorem_ipsum = '''# Lorem ipsum 

## dolor sit amet, consectetur adipiscing elit. 

Duis ante diam, dapibus sed congue id, dignissim non magna. Praesent id elit ipsum, ut porta mauris. Fusce eu ante nec nisl mollis ornare id id tortor. Nulla blandit molestie tempus. Vivamus eu pharetra magna. Etiam molestie, urna eu luctus pharetra, elit nulla tristique nulla, eget eleifend erat ipsum id purus. Nullam tristique accumsan pretium. Maecenas mauris dolor, commodo vitae malesuada feugiat, cursus ac nulla. Suspendisse laoreet scelerisque dapibus. Integer consequat consectetur est vitae laoreet. Donec ultricies gravida risus, non vulputate tortor accumsan id.

### Donec nec tellus nunc, sed egestas libero. Curabitur commodo volutpat orci, eu accumsan lacus feugiat at. 

Suspendisse eu bibendum ante. Etiam sed nisl quis quam iaculis varius. Donec vulputate leo est. Suspendisse varius tortor quis leo auctor in ullamcorper augue lobortis. Vivamus vel dui at nibh semper convallis vel ut odio. Pellentesque convallis scelerisque dolor a pretium.

### Nam ultrices nisl eu dolor vulputate sit amet hendrerit massa euismod. Aenean a tempor lacus.

 Phasellus aliquet magna pellentesque sapien rhoncus malesuada. Donec elementum convallis augue auctor fringilla. In pretium, nibh sed feugiat venenatis, massa eros aliquet libero, ac lacinia turpis eros consequat sapien. Quisque at ligula arcu. Phasellus accumsan tempus enim ut laoreet. Nam orci tortor, bibendum in pharetra in, dignissim at erat. Vestibulum egestas consequat turpis, non viverra diam vehicula at. Nam rutrum laoreet eleifend. Mauris non augue in elit sollicitudin accumsan. Ut est neque, fringilla tincidunt ultrices et, vestibulum vitae sem. Ut ac risus at nisi tristique rhoncus eget at velit. Ut mauris massa, mattis non molestie pretium, cursus nec ipsum. Nullam venenatis magna et sapien malesuada bibendum. Vestibulum fermentum bibendum egestas.

# Sed venenatis, tortor vel faucibus egestas, urna neque bibendum neque, eget porta ante nisi et nulla. 

Nulla ipsum dolor, scelerisque quis aliquet at, congue quis ligula. Mauris sapien mauris, lacinia ac ultricies ut, scelerisque ut ante. Aliquam non tellus lectus. Aliquam condimentum aliquet luctus. Aliquam dapibus rutrum lacinia. Donec a nunc augue. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Sed nec sapien a odio volutpat eleifend. Donec et sem at lectus sollicitudin mattis id at erat. Donec ut orci mi, id feugiat dolor. In nibh lectus, hendrerit ac hendrerit sit amet, porta non mi. Nunc pretium consectetur dui, id cursus orci adipiscing nec. Aliquam vel leo massa. Etiam quam elit, porttitor non interdum in, blandit pellentesque arcu.

Pellentesque faucibus varius purus, at laoreet nisi pulvinar vitae. Morbi faucibus convallis mauris, ut vehicula velit fermentum non. Nam velit felis, fringilla sed viverra in, vestibulum sit amet sem. Vestibulum bibendum nunc vitae magna congue auctor blandit justo dictum. Pellentesque eget arcu et dolor congue consectetur vitae nec lectus. Curabitur sem odio, placerat eget vestibulum non, auctor nec eros. Vestibulum quis quam quis massa vestibulum gravida id vitae est. Aliquam sed varius tellus. Sed non tortor orci.'''

mongo = pymongo.Connection ('localhost', 27017)['sicki']

results = mongo.blog.find ()
for page in results:
    print page['_id']
    mongo.blog.update ({
            '_id': page['_id']
            }, {
            '$set': {
                'body': lorem_ipsum
                }
            })
