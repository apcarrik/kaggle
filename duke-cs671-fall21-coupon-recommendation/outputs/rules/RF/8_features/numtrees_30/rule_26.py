def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Bar, obj[5]: Restaurant20to50, obj[6]: Direction_same, obj[7]: Distance
	# {"feature": "Coupon", "instances": 34, "metric_value": 0.9082, "depth": 1}
	if obj[1]>0:
		# {"feature": "Bar", "instances": 27, "metric_value": 0.6913, "depth": 2}
		if obj[4]<=2.0:
			# {"feature": "Occupation", "instances": 23, "metric_value": 0.4262, "depth": 3}
			if obj[3]>6:
				# {"feature": "Distance", "instances": 13, "metric_value": 0.6194, "depth": 4}
				if obj[7]>1:
					# {"feature": "Restaurant20to50", "instances": 8, "metric_value": 0.8113, "depth": 5}
					if obj[5]<=1.0:
						# {"feature": "Direction_same", "instances": 6, "metric_value": 0.9183, "depth": 6}
						if obj[6]<=0:
							# {"feature": "Passanger", "instances": 5, "metric_value": 0.971, "depth": 7}
							if obj[0]<=1:
								# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[2]>1:
									return 'False'
								elif obj[2]<=1:
									return 'True'
								else: return 'True'
							elif obj[0]>1:
								# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[2]<=0:
									return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[6]>0:
							return 'True'
						else: return 'True'
					elif obj[5]>1.0:
						return 'True'
					else: return 'True'
				elif obj[7]<=1:
					return 'True'
				else: return 'True'
			elif obj[3]<=6:
				return 'True'
			else: return 'True'
		elif obj[4]>2.0:
			# {"feature": "Direction_same", "instances": 4, "metric_value": 0.8113, "depth": 3}
			if obj[6]<=0:
				return 'False'
			elif obj[6]>0:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[1]<=0:
		# {"feature": "Occupation", "instances": 7, "metric_value": 0.5917, "depth": 2}
		if obj[3]>2:
			return 'False'
		elif obj[3]<=2:
			return 'True'
		else: return 'True'
	else: return 'False'
