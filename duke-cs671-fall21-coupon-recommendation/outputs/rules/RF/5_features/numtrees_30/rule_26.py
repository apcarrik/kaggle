def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Restaurant20to50, obj[4]: Distance
	# {"feature": "Coupon", "instances": 34, "metric_value": 0.9082, "depth": 1}
	if obj[0]<=2:
		# {"feature": "Education", "instances": 17, "metric_value": 0.5226, "depth": 2}
		if obj[1]<=0:
			# {"feature": "Occupation", "instances": 9, "metric_value": 0.7642, "depth": 3}
			if obj[2]>4:
				# {"feature": "Distance", "instances": 8, "metric_value": 0.5436, "depth": 4}
				if obj[4]>1:
					# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 0.65, "depth": 5}
					if obj[3]<=1.0:
						return 'True'
					elif obj[3]>1.0:
						return 'True'
					else: return 'True'
				elif obj[4]<=1:
					return 'True'
				else: return 'True'
			elif obj[2]<=4:
				return 'False'
			else: return 'False'
		elif obj[1]>0:
			return 'True'
		else: return 'True'
	elif obj[0]>2:
		# {"feature": "Restaurant20to50", "instances": 17, "metric_value": 0.9975, "depth": 2}
		if obj[3]<=3.0:
			# {"feature": "Distance", "instances": 15, "metric_value": 0.971, "depth": 3}
			if obj[4]>1:
				# {"feature": "Occupation", "instances": 13, "metric_value": 0.9957, "depth": 4}
				if obj[2]<=12:
					# {"feature": "Education", "instances": 12, "metric_value": 0.9799, "depth": 5}
					if obj[1]<=2:
						return 'True'
					elif obj[1]>2:
						return 'False'
					else: return 'False'
				elif obj[2]>12:
					return 'True'
				else: return 'True'
			elif obj[4]<=1:
				return 'False'
			else: return 'False'
		elif obj[3]>3.0:
			return 'True'
		else: return 'True'
	else: return 'False'
