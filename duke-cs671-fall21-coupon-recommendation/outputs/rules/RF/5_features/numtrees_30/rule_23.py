def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Restaurant20to50, obj[4]: Distance
	# {"feature": "Education", "instances": 34, "metric_value": 0.9367, "depth": 1}
	if obj[1]<=3:
		# {"feature": "Occupation", "instances": 31, "metric_value": 0.9629, "depth": 2}
		if obj[2]<=12:
			# {"feature": "Coupon", "instances": 29, "metric_value": 0.9784, "depth": 3}
			if obj[0]<=3:
				# {"feature": "Restaurant20to50", "instances": 18, "metric_value": 0.9183, "depth": 4}
				if obj[3]>0.0:
					# {"feature": "Distance", "instances": 17, "metric_value": 0.874, "depth": 5}
					if obj[4]>1:
						return 'True'
					elif obj[4]<=1:
						return 'True'
					else: return 'True'
				elif obj[3]<=0.0:
					return 'False'
				else: return 'False'
			elif obj[0]>3:
				# {"feature": "Distance", "instances": 11, "metric_value": 0.994, "depth": 4}
				if obj[4]<=2:
					# {"feature": "Restaurant20to50", "instances": 10, "metric_value": 1.0, "depth": 5}
					if obj[3]>0.0:
						return 'False'
					elif obj[3]<=0.0:
						return 'True'
					else: return 'True'
				elif obj[4]>2:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[2]>12:
			return 'True'
		else: return 'True'
	elif obj[1]>3:
		return 'True'
	else: return 'True'
