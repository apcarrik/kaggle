def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Bar, obj[9]: Coffeehouse, obj[10]: Restaurant20to50, obj[11]: Direction_same, obj[12]: Distance
	# {"feature": "Direction_same", "instances": 23, "metric_value": 0.9656, "depth": 1}
	if obj[11]<=0:
		# {"feature": "Distance", "instances": 19, "metric_value": 0.998, "depth": 2}
		if obj[12]>1:
			# {"feature": "Bar", "instances": 14, "metric_value": 0.8631, "depth": 3}
			if obj[8]<=0.0:
				# {"feature": "Gender", "instances": 7, "metric_value": 0.9852, "depth": 4}
				if obj[3]<=0:
					return 'True'
				elif obj[3]>0:
					return 'False'
				else: return 'False'
			elif obj[8]>0.0:
				return 'False'
			else: return 'False'
		elif obj[12]<=1:
			return 'True'
		else: return 'True'
	elif obj[11]>0:
		return 'False'
	else: return 'False'
