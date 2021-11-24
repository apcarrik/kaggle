def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Bar, obj[9]: Coffeehouse, obj[10]: Restaurant20to50, obj[11]: Direction_same, obj[12]: Distance
	# {"feature": "Direction_same", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[11]<=0:
		# {"feature": "Age", "instances": 19, "metric_value": 0.9819, "depth": 2}
		if obj[4]<=2:
			# {"feature": "Passanger", "instances": 10, "metric_value": 0.469, "depth": 3}
			if obj[0]<=2:
				return 'False'
			elif obj[0]>2:
				return 'True'
			else: return 'True'
		elif obj[4]>2:
			# {"feature": "Bar", "instances": 9, "metric_value": 0.7642, "depth": 3}
			if obj[8]>0.0:
				return 'True'
			elif obj[8]<=0.0:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[11]>0:
		return 'True'
	else: return 'True'
