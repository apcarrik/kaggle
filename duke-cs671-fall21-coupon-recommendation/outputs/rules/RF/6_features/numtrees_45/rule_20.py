def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Distance
	# {"feature": "Passanger", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[0]<=1:
		# {"feature": "Restaurant20to50", "instances": 15, "metric_value": 0.9183, "depth": 2}
		if obj[4]<=1.0:
			# {"feature": "Distance", "instances": 9, "metric_value": 0.5033, "depth": 3}
			if obj[5]<=2:
				return 'False'
			elif obj[5]>2:
				return 'True'
			else: return 'True'
		elif obj[4]>1.0:
			# {"feature": "Coupon", "instances": 6, "metric_value": 0.9183, "depth": 3}
			if obj[1]<=2:
				# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[2]>0:
					return 'False'
				elif obj[2]<=0:
					return 'True'
				else: return 'True'
			elif obj[1]>2:
				return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[0]>1:
		# {"feature": "Restaurant20to50", "instances": 8, "metric_value": 0.5436, "depth": 2}
		if obj[4]<=1.0:
			return 'True'
		elif obj[4]>1.0:
			return 'False'
		else: return 'False'
	else: return 'True'
