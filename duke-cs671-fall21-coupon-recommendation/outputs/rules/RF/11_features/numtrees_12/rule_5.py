def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Age, obj[4]: Education, obj[5]: Occupation, obj[6]: Bar, obj[7]: Coffeehouse, obj[8]: Restaurant20to50, obj[9]: Direction_same, obj[10]: Distance
	# {"feature": "Passanger", "instances": 85, "metric_value": 0.9919, "depth": 1}
	if obj[0]<=1:
		# {"feature": "Occupation", "instances": 55, "metric_value": 0.9883, "depth": 2}
		if obj[5]<=11:
			# {"feature": "Coupon", "instances": 50, "metric_value": 0.9988, "depth": 3}
			if obj[2]<=3:
				# {"feature": "Education", "instances": 32, "metric_value": 0.9745, "depth": 4}
				if obj[4]>0:
					# {"feature": "Coffeehouse", "instances": 23, "metric_value": 0.9986, "depth": 5}
					if obj[7]<=3.0:
						# {"feature": "Restaurant20to50", "instances": 21, "metric_value": 0.9984, "depth": 6}
						if obj[8]>-1.0:
							# {"feature": "Bar", "instances": 19, "metric_value": 0.9819, "depth": 7}
							if obj[6]<=1.0:
								# {"feature": "Time", "instances": 14, "metric_value": 0.9852, "depth": 8}
								if obj[1]<=2:
									# {"feature": "Direction_same", "instances": 10, "metric_value": 0.971, "depth": 9}
									if obj[9]<=0:
										# {"feature": "Age", "instances": 8, "metric_value": 0.8113, "depth": 10}
										if obj[3]<=3:
											return 'True'
										elif obj[3]>3:
											# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[10]>2:
												return 'True'
											elif obj[10]<=2:
												return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[9]>0:
										return 'False'
									else: return 'False'
								elif obj[1]>2:
									return 'False'
								else: return 'False'
							elif obj[6]>1.0:
								return 'True'
							else: return 'True'
						elif obj[8]<=-1.0:
							return 'False'
						else: return 'False'
					elif obj[7]>3.0:
						return 'False'
					else: return 'False'
				elif obj[4]<=0:
					# {"feature": "Age", "instances": 9, "metric_value": 0.5033, "depth": 5}
					if obj[3]>0:
						return 'True'
					elif obj[3]<=0:
						# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[1]<=3:
							return 'False'
						elif obj[1]>3:
							return 'True'
						else: return 'True'
					else: return 'False'
				else: return 'True'
			elif obj[2]>3:
				# {"feature": "Coffeehouse", "instances": 18, "metric_value": 0.8524, "depth": 4}
				if obj[7]<=2.0:
					# {"feature": "Bar", "instances": 14, "metric_value": 0.5917, "depth": 5}
					if obj[6]>-1.0:
						# {"feature": "Education", "instances": 13, "metric_value": 0.3912, "depth": 6}
						if obj[4]<=3:
							return 'False'
						elif obj[4]>3:
							# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[1]>1:
								return 'True'
							elif obj[1]<=1:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[6]<=-1.0:
						return 'True'
					else: return 'True'
				elif obj[7]>2.0:
					# {"feature": "Time", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[1]>0:
						return 'True'
					elif obj[1]<=0:
						return 'False'
					else: return 'False'
				else: return 'True'
			else: return 'False'
		elif obj[5]>11:
			return 'False'
		else: return 'False'
	elif obj[0]>1:
		# {"feature": "Coffeehouse", "instances": 30, "metric_value": 0.7838, "depth": 2}
		if obj[7]<=2.0:
			# {"feature": "Occupation", "instances": 22, "metric_value": 0.5746, "depth": 3}
			if obj[5]<=12:
				# {"feature": "Coupon", "instances": 19, "metric_value": 0.2975, "depth": 4}
				if obj[2]>0:
					return 'True'
				elif obj[2]<=0:
					# {"feature": "Age", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[3]>1:
						return 'True'
					elif obj[3]<=1:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[5]>12:
				# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[3]>0:
					return 'False'
				elif obj[3]<=0:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[7]>2.0:
			# {"feature": "Coupon", "instances": 8, "metric_value": 1.0, "depth": 3}
			if obj[2]>2:
				# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[8]>0.0:
					return 'True'
				elif obj[8]<=0.0:
					return 'False'
				else: return 'False'
			elif obj[2]<=2:
				return 'False'
			else: return 'False'
		else: return 'False'
	else: return 'True'
