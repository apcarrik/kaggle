def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Restaurant20to50, obj[4]: Distance
	# {"feature": "Education", "instances": 34, "metric_value": 0.9597, "depth": 1}
	if obj[1]<=1:
		# {"feature": "Occupation", "instances": 17, "metric_value": 0.5226, "depth": 2}
		if obj[2]<=18:
			# {"feature": "Restaurant20to50", "instances": 16, "metric_value": 0.3373, "depth": 3}
			if obj[3]<=1.0:
				return 'True'
			elif obj[3]>1.0:
				# {"feature": "Coupon", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[0]>1:
					return 'True'
				elif obj[0]<=1:
					# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[4]<=1:
						return 'False'
					elif obj[4]>1:
						return 'True'
					else: return 'True'
				else: return 'False'
			else: return 'True'
		elif obj[2]>18:
			return 'False'
		else: return 'False'
	elif obj[1]>1:
		# {"feature": "Coupon", "instances": 17, "metric_value": 0.9367, "depth": 2}
		if obj[0]>0:
			# {"feature": "Restaurant20to50", "instances": 14, "metric_value": 0.9852, "depth": 3}
			if obj[3]>0.0:
				# {"feature": "Occupation", "instances": 12, "metric_value": 1.0, "depth": 4}
				if obj[2]>4:
					# {"feature": "Distance", "instances": 10, "metric_value": 0.971, "depth": 5}
					if obj[4]>1:
						return 'False'
					elif obj[4]<=1:
						return 'False'
					else: return 'False'
				elif obj[2]<=4:
					return 'True'
				else: return 'True'
			elif obj[3]<=0.0:
				return 'False'
			else: return 'False'
		elif obj[0]<=0:
			return 'False'
		else: return 'False'
	else: return 'False'
