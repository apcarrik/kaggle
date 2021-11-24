def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Bar, obj[5]: Restaurant20to50, obj[6]: Direction_same, obj[7]: Distance
	# {"feature": "Passanger", "instances": 51, "metric_value": 0.9997, "depth": 1}
	if obj[0]<=2:
		# {"feature": "Occupation", "instances": 37, "metric_value": 0.9569, "depth": 2}
		if obj[3]>1:
			# {"feature": "Restaurant20to50", "instances": 32, "metric_value": 0.896, "depth": 3}
			if obj[5]<=1.0:
				# {"feature": "Bar", "instances": 25, "metric_value": 0.971, "depth": 4}
				if obj[4]<=2.0:
					# {"feature": "Education", "instances": 23, "metric_value": 0.9877, "depth": 5}
					if obj[2]<=3:
						# {"feature": "Coupon", "instances": 22, "metric_value": 0.976, "depth": 6}
						if obj[1]<=3:
							# {"feature": "Distance", "instances": 14, "metric_value": 1.0, "depth": 7}
							if obj[7]>1:
								# {"feature": "Direction_same", "instances": 8, "metric_value": 0.9544, "depth": 8}
								if obj[6]<=0:
									return 'False'
								elif obj[6]>0:
									return 'False'
								else: return 'False'
							elif obj[7]<=1:
								# {"feature": "Direction_same", "instances": 6, "metric_value": 0.9183, "depth": 8}
								if obj[6]>0:
									return 'True'
								elif obj[6]<=0:
									return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[1]>3:
							# {"feature": "Distance", "instances": 8, "metric_value": 0.8113, "depth": 7}
							if obj[7]>1:
								# {"feature": "Direction_same", "instances": 5, "metric_value": 0.971, "depth": 8}
								if obj[6]<=0:
									return 'False'
								else: return 'False'
							elif obj[7]<=1:
								return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[2]>3:
						return 'True'
					else: return 'True'
				elif obj[4]>2.0:
					return 'False'
				else: return 'False'
			elif obj[5]>1.0:
				return 'False'
			else: return 'False'
		elif obj[3]<=1:
			# {"feature": "Coupon", "instances": 5, "metric_value": 0.7219, "depth": 3}
			if obj[1]>0:
				return 'True'
			elif obj[1]<=0:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[0]>2:
		# {"feature": "Coupon", "instances": 14, "metric_value": 0.7496, "depth": 2}
		if obj[1]<=3:
			return 'True'
		elif obj[1]>3:
			# {"feature": "Occupation", "instances": 4, "metric_value": 0.8113, "depth": 3}
			if obj[3]<=5:
				# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[5]>1.0:
					return 'True'
				elif obj[5]<=1.0:
					return 'False'
				else: return 'False'
			elif obj[3]>5:
				return 'False'
			else: return 'False'
		else: return 'False'
	else: return 'True'
