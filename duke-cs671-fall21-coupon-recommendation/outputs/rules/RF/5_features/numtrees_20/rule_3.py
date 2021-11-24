def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Restaurant20to50, obj[4]: Distance
	# {"feature": "Occupation", "instances": 51, "metric_value": 0.9367, "depth": 1}
	if obj[2]<=11:
		# {"feature": "Education", "instances": 40, "metric_value": 0.9928, "depth": 2}
		if obj[1]<=3:
			# {"feature": "Distance", "instances": 37, "metric_value": 0.9995, "depth": 3}
			if obj[4]<=2:
				# {"feature": "Coupon", "instances": 33, "metric_value": 0.9834, "depth": 4}
				if obj[0]>1:
					# {"feature": "Restaurant20to50", "instances": 24, "metric_value": 0.9183, "depth": 5}
					if obj[3]>-1.0:
						return 'True'
					elif obj[3]<=-1.0:
						return 'False'
					else: return 'False'
				elif obj[0]<=1:
					# {"feature": "Restaurant20to50", "instances": 9, "metric_value": 0.9183, "depth": 5}
					if obj[3]<=2.0:
						return 'False'
					elif obj[3]>2.0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[4]>2:
				return 'False'
			else: return 'False'
		elif obj[1]>3:
			return 'True'
		else: return 'True'
	elif obj[2]>11:
		return 'True'
	else: return 'True'
