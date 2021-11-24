def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Coffeehouse, obj[7]: Restaurant20to50, obj[8]: Direction_same, obj[9]: Distance
	# {"feature": "Occupation", "instances": 85, "metric_value": 0.9999, "depth": 1}
	if obj[4]>1:
		# {"feature": "Restaurant20to50", "instances": 75, "metric_value": 0.9937, "depth": 2}
		if obj[7]>0.0:
			# {"feature": "Passanger", "instances": 67, "metric_value": 0.9998, "depth": 3}
			if obj[0]<=2:
				# {"feature": "Time", "instances": 47, "metric_value": 0.9734, "depth": 4}
				if obj[1]<=1:
					# {"feature": "Distance", "instances": 29, "metric_value": 0.9923, "depth": 5}
					if obj[9]>1:
						# {"feature": "Coupon", "instances": 15, "metric_value": 0.9183, "depth": 6}
						if obj[2]>2:
							# {"feature": "Education", "instances": 8, "metric_value": 1.0, "depth": 7}
							if obj[3]<=1:
								# {"feature": "Bar", "instances": 6, "metric_value": 0.9183, "depth": 8}
								if obj[5]<=1.0:
									# {"feature": "Coffeehouse", "instances": 5, "metric_value": 0.7219, "depth": 9}
									if obj[6]>0.0:
										return 'False'
									elif obj[6]<=0.0:
										# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[5]>1.0:
									return 'True'
								else: return 'True'
							elif obj[3]>1:
								return 'True'
							else: return 'True'
						elif obj[2]<=2:
							# {"feature": "Direction_same", "instances": 7, "metric_value": 0.5917, "depth": 7}
							if obj[8]<=0:
								return 'False'
							elif obj[8]>0:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[9]<=1:
						# {"feature": "Coupon", "instances": 14, "metric_value": 0.7496, "depth": 6}
						if obj[2]>3:
							# {"feature": "Education", "instances": 8, "metric_value": 0.9544, "depth": 7}
							if obj[3]>1:
								# {"feature": "Bar", "instances": 6, "metric_value": 0.65, "depth": 8}
								if obj[5]<=1.0:
									return 'True'
								elif obj[5]>1.0:
									# {"feature": "Coffeehouse", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[6]<=2.0:
										return 'False'
									elif obj[6]>2.0:
										return 'True'
									else: return 'True'
								else: return 'False'
							elif obj[3]<=1:
								return 'False'
							else: return 'False'
						elif obj[2]<=3:
							return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[1]>1:
					# {"feature": "Coupon", "instances": 18, "metric_value": 0.65, "depth": 5}
					if obj[2]>1:
						# {"feature": "Bar", "instances": 12, "metric_value": 0.8113, "depth": 6}
						if obj[5]<=2.0:
							# {"feature": "Direction_same", "instances": 9, "metric_value": 0.9183, "depth": 7}
							if obj[8]<=0:
								# {"feature": "Education", "instances": 6, "metric_value": 1.0, "depth": 8}
								if obj[3]>0:
									# {"feature": "Distance", "instances": 5, "metric_value": 0.971, "depth": 9}
									if obj[9]<=2:
										# {"feature": "Coffeehouse", "instances": 4, "metric_value": 0.8113, "depth": 10}
										if obj[6]<=1.0:
											return 'True'
										elif obj[6]>1.0:
											return 'True'
										else: return 'True'
									elif obj[9]>2:
										return 'False'
									else: return 'False'
								elif obj[3]<=0:
									return 'False'
								else: return 'False'
							elif obj[8]>0:
								return 'False'
							else: return 'False'
						elif obj[5]>2.0:
							return 'False'
						else: return 'False'
					elif obj[2]<=1:
						return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[0]>2:
				# {"feature": "Coffeehouse", "instances": 20, "metric_value": 0.8113, "depth": 4}
				if obj[6]<=2.0:
					# {"feature": "Education", "instances": 15, "metric_value": 0.9183, "depth": 5}
					if obj[3]<=0:
						# {"feature": "Time", "instances": 8, "metric_value": 0.5436, "depth": 6}
						if obj[1]<=3:
							return 'True'
						elif obj[1]>3:
							# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[2]<=3:
								return 'True'
							elif obj[2]>3:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[3]>0:
						# {"feature": "Time", "instances": 7, "metric_value": 0.9852, "depth": 6}
						if obj[1]<=2:
							# {"feature": "Distance", "instances": 5, "metric_value": 0.971, "depth": 7}
							if obj[9]<=1:
								# {"feature": "Bar", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[5]<=1.0:
									return 'False'
								elif obj[5]>1.0:
									return 'True'
								else: return 'True'
							elif obj[9]>1:
								return 'True'
							else: return 'True'
						elif obj[1]>2:
							return 'False'
						else: return 'False'
					else: return 'False'
				elif obj[6]>2.0:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[7]<=0.0:
			return 'False'
		else: return 'False'
	elif obj[4]<=1:
		# {"feature": "Coffeehouse", "instances": 10, "metric_value": 0.469, "depth": 2}
		if obj[6]<=2.0:
			return 'True'
		elif obj[6]>2.0:
			return 'False'
		else: return 'False'
	else: return 'True'
