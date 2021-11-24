def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Distance
	# {"feature": "Distance", "instances": 34, "metric_value": 0.874, "depth": 1}
	if obj[5]<=2:
		# {"feature": "Occupation", "instances": 32, "metric_value": 0.8113, "depth": 2}
		if obj[3]<=9:
			# {"feature": "Coupon", "instances": 24, "metric_value": 0.65, "depth": 3}
			if obj[1]>1:
				# {"feature": "Education", "instances": 19, "metric_value": 0.2975, "depth": 4}
				if obj[2]>1:
					return 'True'
				elif obj[2]<=1:
					# {"feature": "Passanger", "instances": 9, "metric_value": 0.5033, "depth": 5}
					if obj[0]<=1:
						# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 0.65, "depth": 6}
						if obj[4]<=1.0:
							return 'True'
						elif obj[4]>1.0:
							return 'True'
						else: return 'True'
					elif obj[0]>1:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[1]<=1:
				# {"feature": "Passanger", "instances": 5, "metric_value": 0.971, "depth": 4}
				if obj[0]>0:
					# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[4]<=1.0:
						return 'False'
					elif obj[4]>1.0:
						return 'True'
					else: return 'True'
				elif obj[0]<=0:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[3]>9:
			# {"feature": "Coupon", "instances": 8, "metric_value": 1.0, "depth": 3}
			if obj[1]>2:
				# {"feature": "Education", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[2]>0:
					return 'False'
				elif obj[2]<=0:
					# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[0]<=1:
						return 'False'
					elif obj[0]>1:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[1]<=2:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[5]>2:
		return 'False'
	else: return 'False'
