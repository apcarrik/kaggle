def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Coffeehouse, obj[7]: Restaurant20to50, obj[8]: Direction_same, obj[9]: Distance
	# {"feature": "Distance", "instances": 85, "metric_value": 0.9637, "depth": 1}
	if obj[9]>1:
		# {"feature": "Occupation", "instances": 52, "metric_value": 1.0, "depth": 2}
		if obj[4]<=8:
			# {"feature": "Bar", "instances": 37, "metric_value": 0.974, "depth": 3}
			if obj[5]<=2.0:
				# {"feature": "Coffeehouse", "instances": 31, "metric_value": 0.9992, "depth": 4}
				if obj[6]<=2.0:
					# {"feature": "Education", "instances": 24, "metric_value": 0.9544, "depth": 5}
					if obj[3]<=2:
						# {"feature": "Coupon", "instances": 18, "metric_value": 0.8524, "depth": 6}
						if obj[2]>0:
							# {"feature": "Restaurant20to50", "instances": 14, "metric_value": 0.5917, "depth": 7}
							if obj[7]<=1.0:
								# {"feature": "Time", "instances": 10, "metric_value": 0.7219, "depth": 8}
								if obj[1]<=2:
									# {"feature": "Passanger", "instances": 8, "metric_value": 0.8113, "depth": 9}
									if obj[0]<=1:
										# {"feature": "Direction_same", "instances": 5, "metric_value": 0.7219, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									elif obj[0]>1:
										# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[1]>2:
									return 'True'
								else: return 'True'
							elif obj[7]>1.0:
								return 'True'
							else: return 'True'
						elif obj[2]<=0:
							# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[0]<=1:
								return 'False'
							elif obj[0]>1:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[3]>2:
						# {"feature": "Passanger", "instances": 6, "metric_value": 0.9183, "depth": 6}
						if obj[0]<=1:
							# {"feature": "Coupon", "instances": 4, "metric_value": 1.0, "depth": 7}
							if obj[2]<=3:
								return 'True'
							elif obj[2]>3:
								return 'False'
							else: return 'False'
						elif obj[0]>1:
							return 'False'
						else: return 'False'
					else: return 'False'
				elif obj[6]>2.0:
					# {"feature": "Time", "instances": 7, "metric_value": 0.5917, "depth": 5}
					if obj[1]<=3:
						return 'False'
					elif obj[1]>3:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[5]>2.0:
				return 'True'
			else: return 'True'
		elif obj[4]>8:
			# {"feature": "Passanger", "instances": 15, "metric_value": 0.8366, "depth": 3}
			if obj[0]<=2:
				# {"feature": "Time", "instances": 11, "metric_value": 0.9457, "depth": 4}
				if obj[1]<=2:
					# {"feature": "Direction_same", "instances": 9, "metric_value": 0.7642, "depth": 5}
					if obj[8]<=0:
						return 'False'
					elif obj[8]>0:
						# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[2]<=0:
							return 'True'
						elif obj[2]>0:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[1]>2:
					return 'True'
				else: return 'True'
			elif obj[0]>2:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[9]<=1:
		# {"feature": "Time", "instances": 33, "metric_value": 0.7455, "depth": 2}
		if obj[1]>0:
			# {"feature": "Restaurant20to50", "instances": 23, "metric_value": 0.5586, "depth": 3}
			if obj[7]<=1.0:
				# {"feature": "Education", "instances": 13, "metric_value": 0.7793, "depth": 4}
				if obj[3]<=1:
					# {"feature": "Coupon", "instances": 10, "metric_value": 0.469, "depth": 5}
					if obj[2]>0:
						return 'True'
					elif obj[2]<=0:
						return 'False'
					else: return 'False'
				elif obj[3]>1:
					# {"feature": "Coffeehouse", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[6]<=3.0:
						return 'False'
					elif obj[6]>3.0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[7]>1.0:
				return 'True'
			else: return 'True'
		elif obj[1]<=0:
			# {"feature": "Passanger", "instances": 10, "metric_value": 0.971, "depth": 3}
			if obj[0]<=1:
				# {"feature": "Occupation", "instances": 6, "metric_value": 0.9183, "depth": 4}
				if obj[4]>10:
					# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[2]>0:
						# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[3]>0:
							return 'True'
						elif obj[3]<=0:
							return 'False'
						else: return 'False'
					elif obj[2]<=0:
						return 'True'
					else: return 'True'
				elif obj[4]<=10:
					return 'False'
				else: return 'False'
			elif obj[0]>1:
				return 'True'
			else: return 'True'
		else: return 'True'
	else: return 'True'
