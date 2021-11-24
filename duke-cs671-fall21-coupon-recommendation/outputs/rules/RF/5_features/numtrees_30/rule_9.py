def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Restaurant20to50, obj[4]: Distance
	# {"feature": "Coupon", "instances": 34, "metric_value": 0.9975, "depth": 1}
	if obj[0]>0:
		# {"feature": "Education", "instances": 30, "metric_value": 0.971, "depth": 2}
		if obj[1]<=2:
			# {"feature": "Occupation", "instances": 25, "metric_value": 0.9044, "depth": 3}
			if obj[2]<=12:
				# {"feature": "Restaurant20to50", "instances": 23, "metric_value": 0.8281, "depth": 4}
				if obj[3]<=2.0:
					# {"feature": "Distance", "instances": 22, "metric_value": 0.7732, "depth": 5}
					if obj[4]<=2:
						return 'True'
					elif obj[4]>2:
						return 'True'
					else: return 'True'
				elif obj[3]>2.0:
					return 'False'
				else: return 'False'
			elif obj[2]>12:
				return 'False'
			else: return 'False'
		elif obj[1]>2:
			# {"feature": "Occupation", "instances": 5, "metric_value": 0.7219, "depth": 3}
			if obj[2]>1:
				return 'False'
			elif obj[2]<=1:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[0]<=0:
		return 'False'
	else: return 'False'
