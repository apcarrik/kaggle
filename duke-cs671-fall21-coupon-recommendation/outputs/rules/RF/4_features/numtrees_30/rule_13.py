def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Distance
	# {"feature": "Education", "instances": 34, "metric_value": 0.9975, "depth": 1}
	if obj[1]<=2:
		# {"feature": "Coupon", "instances": 26, "metric_value": 0.9306, "depth": 2}
		if obj[0]<=3:
			# {"feature": "Occupation", "instances": 15, "metric_value": 0.7219, "depth": 3}
			if obj[2]<=18:
				# {"feature": "Distance", "instances": 14, "metric_value": 0.5917, "depth": 4}
				if obj[3]<=2:
					return 'True'
				elif obj[3]>2:
					return 'True'
				else: return 'True'
			elif obj[2]>18:
				return 'False'
			else: return 'False'
		elif obj[0]>3:
			# {"feature": "Occupation", "instances": 11, "metric_value": 0.994, "depth": 3}
			if obj[2]<=7:
				# {"feature": "Distance", "instances": 6, "metric_value": 0.9183, "depth": 4}
				if obj[3]<=1:
					return 'True'
				elif obj[3]>1:
					return 'False'
				else: return 'False'
			elif obj[2]>7:
				# {"feature": "Distance", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[3]<=1:
					return 'False'
				else: return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[1]>2:
		# {"feature": "Coupon", "instances": 8, "metric_value": 0.5436, "depth": 2}
		if obj[0]>0:
			return 'False'
		elif obj[0]<=0:
			return 'True'
		else: return 'True'
	else: return 'False'
