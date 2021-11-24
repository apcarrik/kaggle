def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Restaurant20to50, obj[4]: Distance
	# {"feature": "Restaurant20to50", "instances": 34, "metric_value": 0.9975, "depth": 1}
	if obj[3]<=1.0:
		# {"feature": "Occupation", "instances": 19, "metric_value": 0.8997, "depth": 2}
		if obj[2]<=12:
			# {"feature": "Coupon", "instances": 17, "metric_value": 0.7871, "depth": 3}
			if obj[0]<=2:
				# {"feature": "Education", "instances": 10, "metric_value": 0.971, "depth": 4}
				if obj[1]>0:
					# {"feature": "Distance", "instances": 8, "metric_value": 1.0, "depth": 5}
					if obj[4]<=2:
						return 'True'
					elif obj[4]>2:
						return 'False'
					else: return 'False'
				elif obj[1]<=0:
					return 'False'
				else: return 'False'
			elif obj[0]>2:
				return 'False'
			else: return 'False'
		elif obj[2]>12:
			return 'True'
		else: return 'True'
	elif obj[3]>1.0:
		# {"feature": "Education", "instances": 15, "metric_value": 0.7219, "depth": 2}
		if obj[1]<=2:
			# {"feature": "Coupon", "instances": 12, "metric_value": 0.4138, "depth": 3}
			if obj[0]<=3:
				return 'True'
			elif obj[0]>3:
				# {"feature": "Occupation", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[2]<=5:
					return 'True'
				elif obj[2]>5:
					# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[4]>1:
						return 'True'
					elif obj[4]<=1:
						return 'False'
					else: return 'False'
				else: return 'True'
			else: return 'True'
		elif obj[1]>2:
			# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 3}
			if obj[0]>0:
				return 'False'
			elif obj[0]<=0:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'True'
