def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Direction_same, obj[6]: Distance
	# {"feature": "Restaurant20to50", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[4]<=1.0:
		# {"feature": "Occupation", "instances": 12, "metric_value": 0.65, "depth": 2}
		if obj[3]>2:
			return 'False'
		elif obj[3]<=2:
			# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 3}
			if obj[1]>1:
				# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[6]<=2:
					return 'False'
				elif obj[6]>2:
					return 'True'
				else: return 'True'
			elif obj[1]<=1:
				return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[4]>1.0:
		# {"feature": "Occupation", "instances": 11, "metric_value": 0.684, "depth": 2}
		if obj[3]<=7:
			return 'True'
		elif obj[3]>7:
			# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 3}
			if obj[2]>0:
				return 'False'
			elif obj[2]<=0:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'True'
