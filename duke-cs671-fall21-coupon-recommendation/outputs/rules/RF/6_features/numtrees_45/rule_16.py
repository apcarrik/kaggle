def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Distance
	# {"feature": "Occupation", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[3]>5:
		# {"feature": "Coupon", "instances": 13, "metric_value": 0.8905, "depth": 2}
		if obj[1]<=3:
			# {"feature": "Passanger", "instances": 8, "metric_value": 0.5436, "depth": 3}
			if obj[0]<=1:
				# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[4]<=1.0:
					# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[5]<=1:
						return 'True'
					elif obj[5]>1:
						return 'False'
					else: return 'False'
				elif obj[4]>1.0:
					return 'True'
				else: return 'True'
			elif obj[0]>1:
				return 'True'
			else: return 'True'
		elif obj[1]>3:
			# {"feature": "Passanger", "instances": 5, "metric_value": 0.971, "depth": 3}
			if obj[0]>1:
				# {"feature": "Education", "instances": 4, "metric_value": 1.0, "depth": 4}
				if obj[2]>1:
					# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[5]>1:
						return 'False'
					elif obj[5]<=1:
						return 'True'
					else: return 'True'
				elif obj[2]<=1:
					return 'True'
				else: return 'True'
			elif obj[0]<=1:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[3]<=5:
		# {"feature": "Coupon", "instances": 10, "metric_value": 0.971, "depth": 2}
		if obj[1]<=3:
			# {"feature": "Passanger", "instances": 7, "metric_value": 0.5917, "depth": 3}
			if obj[0]>0:
				return 'False'
			elif obj[0]<=0:
				return 'True'
			else: return 'True'
		elif obj[1]>3:
			return 'True'
		else: return 'True'
	else: return 'False'
