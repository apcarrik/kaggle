def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Coupon_validity, obj[4]: Gender, obj[5]: Age, obj[6]: Children, obj[7]: Education, obj[8]: Occupation, obj[9]: Income, obj[10]: Bar, obj[11]: Coffeehouse, obj[12]: Restaurant20to50, obj[13]: Direction_same, obj[14]: Distance
	# {"feature": "Distance", "instances": 85, "metric_value": 0.9975, "depth": 1}
	if obj[14]<=2:
		# {"feature": "Occupation", "instances": 73, "metric_value": 0.9693, "depth": 2}
		if obj[8]<=17:
			# {"feature": "Coffeehouse", "instances": 68, "metric_value": 0.9367, "depth": 3}
			if obj[11]>1.0:
				# {"feature": "Income", "instances": 34, "metric_value": 0.7871, "depth": 4}
				if obj[9]<=6:
					# {"feature": "Coupon_validity", "instances": 27, "metric_value": 0.8767, "depth": 5}
					if obj[3]>0:
						# {"feature": "Bar", "instances": 14, "metric_value": 0.9852, "depth": 6}
						if obj[10]<=2.0:
							# {"feature": "Time", "instances": 12, "metric_value": 0.9183, "depth": 7}
							if obj[1]>0:
								# {"feature": "Age", "instances": 9, "metric_value": 0.9911, "depth": 8}
								if obj[5]>1:
									# {"feature": "Education", "instances": 7, "metric_value": 0.9852, "depth": 9}
									if obj[7]>0:
										# {"feature": "Direction_same", "instances": 5, "metric_value": 0.7219, "depth": 10}
										if obj[13]<=0:
											return 'False'
										elif obj[13]>0:
											return 'True'
										else: return 'True'
									elif obj[7]<=0:
										return 'True'
									else: return 'True'
								elif obj[5]<=1:
									return 'True'
								else: return 'True'
							elif obj[1]<=0:
								return 'True'
							else: return 'True'
						elif obj[10]>2.0:
							return 'False'
						else: return 'False'
					elif obj[3]<=0:
						# {"feature": "Coupon", "instances": 13, "metric_value": 0.6194, "depth": 6}
						if obj[2]>0:
							return 'True'
						elif obj[2]<=0:
							# {"feature": "Time", "instances": 4, "metric_value": 1.0, "depth": 7}
							if obj[1]<=0:
								return 'True'
							elif obj[1]>0:
								return 'False'
							else: return 'False'
						else: return 'True'
					else: return 'True'
				elif obj[9]>6:
					return 'True'
				else: return 'True'
			elif obj[11]<=1.0:
				# {"feature": "Restaurant20to50", "instances": 34, "metric_value": 0.9975, "depth": 4}
				if obj[12]>0.0:
					# {"feature": "Time", "instances": 27, "metric_value": 0.951, "depth": 5}
					if obj[1]>0:
						# {"feature": "Income", "instances": 19, "metric_value": 0.998, "depth": 6}
						if obj[9]>1:
							# {"feature": "Coupon", "instances": 15, "metric_value": 0.971, "depth": 7}
							if obj[2]<=3:
								# {"feature": "Education", "instances": 9, "metric_value": 0.9911, "depth": 8}
								if obj[7]<=1:
									# {"feature": "Passanger", "instances": 5, "metric_value": 0.7219, "depth": 9}
									if obj[0]<=2:
										return 'True'
									elif obj[0]>2:
										return 'False'
									else: return 'False'
								elif obj[7]>1:
									# {"feature": "Coupon_validity", "instances": 4, "metric_value": 0.8113, "depth": 9}
									if obj[3]<=0:
										return 'False'
									elif obj[3]>0:
										return 'True'
									else: return 'True'
								else: return 'False'
							elif obj[2]>3:
								# {"feature": "Passanger", "instances": 6, "metric_value": 0.65, "depth": 8}
								if obj[0]>1:
									# {"feature": "Coupon_validity", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[3]<=0:
										# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[6]>0:
											return 'True'
										elif obj[6]<=0:
											return 'False'
										else: return 'False'
									elif obj[3]>0:
										return 'False'
									else: return 'False'
								elif obj[0]<=1:
									return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[9]<=1:
							return 'True'
						else: return 'True'
					elif obj[1]<=0:
						# {"feature": "Income", "instances": 8, "metric_value": 0.5436, "depth": 6}
						if obj[9]>0:
							return 'True'
						elif obj[9]<=0:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[12]<=0.0:
					# {"feature": "Time", "instances": 7, "metric_value": 0.5917, "depth": 5}
					if obj[1]<=3:
						return 'False'
					elif obj[1]>3:
						return 'True'
					else: return 'True'
				else: return 'False'
			else: return 'True'
		elif obj[8]>17:
			return 'False'
		else: return 'False'
	elif obj[14]>2:
		# {"feature": "Passanger", "instances": 12, "metric_value": 0.4138, "depth": 2}
		if obj[0]>0:
			return 'False'
		elif obj[0]<=0:
			return 'True'
		else: return 'True'
	else: return 'False'
