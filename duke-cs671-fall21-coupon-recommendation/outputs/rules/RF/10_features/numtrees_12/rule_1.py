def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Coffeehouse, obj[7]: Restaurant20to50, obj[8]: Direction_same, obj[9]: Distance
	# {"feature": "Occupation", "instances": 85, "metric_value": 0.9879, "depth": 1}
	if obj[4]<=8:
		# {"feature": "Time", "instances": 51, "metric_value": 0.8974, "depth": 2}
		if obj[1]>1:
			# {"feature": "Direction_same", "instances": 26, "metric_value": 0.5159, "depth": 3}
			if obj[8]<=0:
				# {"feature": "Distance", "instances": 25, "metric_value": 0.4022, "depth": 4}
				if obj[9]<=1:
					return 'True'
				elif obj[9]>1:
					# {"feature": "Passanger", "instances": 12, "metric_value": 0.65, "depth": 5}
					if obj[0]>0:
						# {"feature": "Education", "instances": 11, "metric_value": 0.4395, "depth": 6}
						if obj[3]>1:
							# {"feature": "Coupon", "instances": 6, "metric_value": 0.65, "depth": 7}
							if obj[2]<=3:
								# {"feature": "Coffeehouse", "instances": 4, "metric_value": 0.8113, "depth": 8}
								if obj[6]<=1.0:
									return 'True'
								elif obj[6]>1.0:
									# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[5]>1.0:
										return 'True'
									elif obj[5]<=1.0:
										return 'False'
									else: return 'False'
								else: return 'True'
							elif obj[2]>3:
								return 'True'
							else: return 'True'
						elif obj[3]<=1:
							return 'True'
						else: return 'True'
					elif obj[0]<=0:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[8]>0:
				return 'False'
			else: return 'False'
		elif obj[1]<=1:
			# {"feature": "Coupon", "instances": 25, "metric_value": 0.9988, "depth": 3}
			if obj[2]<=3:
				# {"feature": "Distance", "instances": 16, "metric_value": 0.896, "depth": 4}
				if obj[9]<=1:
					# {"feature": "Bar", "instances": 11, "metric_value": 0.994, "depth": 5}
					if obj[5]>0.0:
						# {"feature": "Coffeehouse", "instances": 8, "metric_value": 0.8113, "depth": 6}
						if obj[6]<=2.0:
							return 'True'
						elif obj[6]>2.0:
							# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[7]<=1.0:
								# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[0]<=1:
									# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[3]<=0:
										# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[8]<=1:
											return 'False'
										else: return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[7]>1.0:
								return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[5]<=0.0:
						return 'False'
					else: return 'False'
				elif obj[9]>1:
					return 'True'
				else: return 'True'
			elif obj[2]>3:
				# {"feature": "Bar", "instances": 9, "metric_value": 0.5033, "depth": 4}
				if obj[5]>-1.0:
					return 'False'
				elif obj[5]<=-1.0:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'False'
	elif obj[4]>8:
		# {"feature": "Passanger", "instances": 34, "metric_value": 0.9597, "depth": 2}
		if obj[0]<=1:
			# {"feature": "Bar", "instances": 19, "metric_value": 0.7425, "depth": 3}
			if obj[5]>0.0:
				# {"feature": "Distance", "instances": 13, "metric_value": 0.3912, "depth": 4}
				if obj[9]<=2:
					return 'False'
				elif obj[9]>2:
					# {"feature": "Coupon", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[2]<=2:
						return 'False'
					elif obj[2]>2:
						# {"feature": "Coffeehouse", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[6]>0.0:
							return 'True'
						elif obj[6]<=0.0:
							return 'False'
						else: return 'False'
					else: return 'True'
				else: return 'False'
			elif obj[5]<=0.0:
				# {"feature": "Time", "instances": 6, "metric_value": 1.0, "depth": 4}
				if obj[1]<=1:
					# {"feature": "Coupon", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[2]>0:
						return 'True'
					elif obj[2]<=0:
						return 'False'
					else: return 'False'
				elif obj[1]>1:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[0]>1:
			# {"feature": "Bar", "instances": 15, "metric_value": 0.971, "depth": 3}
			if obj[5]<=1.0:
				# {"feature": "Coffeehouse", "instances": 9, "metric_value": 0.9183, "depth": 4}
				if obj[6]<=1.0:
					# {"feature": "Education", "instances": 7, "metric_value": 0.5917, "depth": 5}
					if obj[3]>2:
						# {"feature": "Time", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[1]<=2:
							# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[2]>2:
								# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[7]<=1.0:
									# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[8]<=0:
										# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[9]<=2:
											return 'False'
										else: return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[2]<=2:
								return 'False'
							else: return 'False'
						elif obj[1]>2:
							return 'False'
						else: return 'False'
					elif obj[3]<=2:
						return 'False'
					else: return 'False'
				elif obj[6]>1.0:
					return 'True'
				else: return 'True'
			elif obj[5]>1.0:
				return 'True'
			else: return 'True'
		else: return 'True'
	else: return 'False'
