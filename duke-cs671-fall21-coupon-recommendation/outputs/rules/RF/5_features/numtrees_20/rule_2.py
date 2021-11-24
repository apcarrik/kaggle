def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Restaurant20to50, obj[4]: Distance
	# {"feature": "Distance", "instances": 51, "metric_value": 0.9774, "depth": 1}
	if obj[4]<=2:
		# {"feature": "Occupation", "instances": 45, "metric_value": 0.9183, "depth": 2}
		if obj[2]<=10:
			# {"feature": "Coupon", "instances": 30, "metric_value": 0.7219, "depth": 3}
			if obj[0]>1:
				# {"feature": "Education", "instances": 24, "metric_value": 0.5436, "depth": 4}
				if obj[1]<=1:
					# {"feature": "Restaurant20to50", "instances": 15, "metric_value": 0.7219, "depth": 5}
					if obj[3]>0.0:
						return 'True'
					elif obj[3]<=0.0:
						return 'True'
					else: return 'True'
				elif obj[1]>1:
					return 'True'
				else: return 'True'
			elif obj[0]<=1:
				# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 1.0, "depth": 4}
				if obj[3]>0.0:
					# {"feature": "Education", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[1]<=2:
						return 'True'
					elif obj[1]>2:
						return 'True'
					else: return 'True'
				elif obj[3]<=0.0:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[2]>10:
			# {"feature": "Education", "instances": 15, "metric_value": 0.971, "depth": 3}
			if obj[1]<=2:
				# {"feature": "Coupon", "instances": 12, "metric_value": 0.8113, "depth": 4}
				if obj[0]<=2:
					# {"feature": "Restaurant20to50", "instances": 9, "metric_value": 0.9183, "depth": 5}
					if obj[3]<=1.0:
						return 'False'
					elif obj[3]>1.0:
						return 'True'
					else: return 'True'
				elif obj[0]>2:
					return 'False'
				else: return 'False'
			elif obj[1]>2:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[4]>2:
		return 'False'
	else: return 'False'
