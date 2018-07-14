using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class StationNamer : MonoBehaviour {

	// Use this for initialization
	void Start () {
		
	}
	
	// Update is called once per frame
	void Update () {
		if (transform.parent != null)
			if (transform.parent.parent != null)
				if (transform.parent.parent.parent != null)
					if (transform.parent.parent.parent.GetComponent<DefaultTrackableEventHandler>() != null)
						GetComponent<Text>().text = "Welcome to " + transform.parent.parent.parent.name + " Station";
	}
}
