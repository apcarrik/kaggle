def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Restaurant20to50, obj[7]: Direction_same, obj[8]: Distance
	# {"feature": "Restaurant20to50", "instances": 51, "metric_value": 0.9975, "depth": 1}
	if obj[6]<=3.0:
		# {"feature": "Occupation", "instances": 48, "metric_value": 0.9887, "depth": 2}
		if obj[4]>2:
			# {"feature": "Bar", "instances": 33, "metric_value": 0.994, "depth": 3}
			if obj[5]>0.0:
				# {"feature": "Time", "instances": 17, "metric_value": 0.9774, "depth": 4}
				if obj[1]<=3:
					# {"feature": "Coupon", "instances": 13, "metric_value": 0.7793, "depth": 5}
					if obj[2]<=1:
						# {"feature": "Passanger", "instances": 8, "metric_value": 0.9544, "depth": 6}
						if obj[0]>0:
							# {"feature": "Education", "instances": 7, "metric_value": 0.9852, "depth": 7}
							if obj[3]>0:
								# {"feature": "Direction_same", "instances": 4, "metric_value": 0.8113, "depth": 8}
								if obj[7]<=0:
									# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[8]<=2:
										return 'False'
									elif obj[8]>2:
										return 'True'
									else: return 'True'
								elif obj[7]>0:
									return 'True'
								else: return 'True'
							elif obj[3]<=0:
								# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[8]>1:
									# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[7]<=0:
										return 'True'
									else: return 'True'
								elif obj[8]<=1:
									return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[0]<=0:
							return 'True'
						else: return 'True'
					elif obj[2]>1:
						return 'True'
					else: return 'True'
				elif obj[1]>3:
					return 'False'
				else: return 'False'
			elif obj[5]<=0.0:
				# {"feature": "Coupon", "instances": 16, "metric_value": 0.896, "depth": 4}
				if obj[2]>2:
					# {"feature": "Time", "instances": 9, "metric_value": 0.9911, "depth": 5}
					if obj[1]<=2:
						# {"feature": "Education", "instances": 7, "metric_value": 0.9852, "depth": 6}
						if obj[3]<=1:
							# {"feature": "Direction_same", "instances": 5, "metric_value": 0.7219, "depth": 7}
							if obj[7]<=0:
								return 'False'
							elif obj[7]>0:
								return 'True'
							else: return 'True'
						elif obj[3]>1:
							return 'True'
						else: return 'True'
					elif obj[1]>2:
						return 'True'
					else: return 'True'
				elif obj[2]<=2:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[4]<=2:
			# {"feature": "Education", "instances": 15, "metric_value": 0.7219, "depth": 3}
			if obj[3]>1:
				return 'True'
			elif obj[3]<=1:
				# {"feature": "Time", "instances": 7, "metric_value": 0.9852, "depth": 4}
				if obj[1]<=3:
					# {"feature": "Coupon", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[2]>0:
						# {"feature": "Bar", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[5]<=0.0:
							return 'True'
						elif obj[5]>0.0:
							return 'False'
						else: return 'False'
					elif obj[2]<=0:
						return 'False'
					else: return 'False'
				elif obj[1]>3:
					return 'True'
				else: return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[6]>3.0:
		return 'False'
	else: return 'False'
