def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Direction_same, obj[6]: Distance
	# {"feature": "Restaurant20to50", "instances": 34, "metric_value": 0.9975, "depth": 1}
	if obj[4]<=3.0:
		# {"feature": "Occupation", "instances": 32, "metric_value": 0.9887, "depth": 2}
		if obj[3]>4:
			# {"feature": "Distance", "instances": 25, "metric_value": 0.9988, "depth": 3}
			if obj[6]>1:
				# {"feature": "Education", "instances": 16, "metric_value": 0.9544, "depth": 4}
				if obj[2]<=4:
					# {"feature": "Passanger", "instances": 15, "metric_value": 0.9183, "depth": 5}
					if obj[0]>0:
						# {"feature": "Direction_same", "instances": 12, "metric_value": 0.9799, "depth": 6}
						if obj[5]<=0:
							# {"feature": "Coupon", "instances": 11, "metric_value": 0.994, "depth": 7}
							if obj[1]>0:
								return 'True'
							elif obj[1]<=0:
								return 'False'
							else: return 'False'
						elif obj[5]>0:
							return 'False'
						else: return 'False'
					elif obj[0]<=0:
						return 'False'
					else: return 'False'
				elif obj[2]>4:
					return 'True'
				else: return 'True'
			elif obj[6]<=1:
				# {"feature": "Passanger", "instances": 9, "metric_value": 0.7642, "depth": 4}
				if obj[0]<=1:
					# {"feature": "Education", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[2]<=0:
						# {"feature": "Coupon", "instances": 4, "metric_value": 1.0, "depth": 6}
						if obj[1]<=3:
							# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[5]<=0:
								return 'True'
							else: return 'True'
						elif obj[1]>3:
							return 'False'
						else: return 'False'
					elif obj[2]>0:
						return 'True'
					else: return 'True'
				elif obj[0]>1:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[3]<=4:
			# {"feature": "Coupon", "instances": 7, "metric_value": 0.5917, "depth": 3}
			if obj[1]<=2:
				return 'False'
			elif obj[1]>2:
				# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[2]>0:
					return 'False'
				elif obj[2]<=0:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'False'
	elif obj[4]>3.0:
		return 'True'
	else: return 'True'
