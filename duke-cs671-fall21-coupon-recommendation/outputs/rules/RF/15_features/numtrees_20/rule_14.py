def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Coupon_validity, obj[4]: Gender, obj[5]: Age, obj[6]: Children, obj[7]: Education, obj[8]: Occupation, obj[9]: Income, obj[10]: Bar, obj[11]: Coffeehouse, obj[12]: Restaurant20to50, obj[13]: Direction_same, obj[14]: Distance
	# {"feature": "Distance", "instances": 51, "metric_value": 0.9526, "depth": 1}
	if obj[14]<=2:
		# {"feature": "Bar", "instances": 41, "metric_value": 0.8722, "depth": 2}
		if obj[10]<=2.0:
			# {"feature": "Coupon", "instances": 35, "metric_value": 0.9275, "depth": 3}
			if obj[2]>1:
				# {"feature": "Occupation", "instances": 29, "metric_value": 0.7973, "depth": 4}
				if obj[8]>5:
					# {"feature": "Time", "instances": 20, "metric_value": 0.9341, "depth": 5}
					if obj[1]>0:
						# {"feature": "Income", "instances": 18, "metric_value": 0.8524, "depth": 6}
						if obj[9]<=6:
							# {"feature": "Passanger", "instances": 14, "metric_value": 0.9403, "depth": 7}
							if obj[0]>0:
								# {"feature": "Coupon_validity", "instances": 13, "metric_value": 0.8905, "depth": 8}
								if obj[3]<=0:
									# {"feature": "Education", "instances": 7, "metric_value": 0.5917, "depth": 9}
									if obj[7]>1:
										return 'True'
									elif obj[7]<=1:
										# {"feature": "Age", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[5]<=2:
											return 'False'
										elif obj[5]>2:
											return 'True'
										else: return 'True'
									else: return 'False'
								elif obj[3]>0:
									# {"feature": "Age", "instances": 6, "metric_value": 1.0, "depth": 9}
									if obj[5]<=6:
										# {"feature": "Coffeehouse", "instances": 5, "metric_value": 0.971, "depth": 10}
										if obj[11]>1.0:
											# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[12]<=1.0:
												return 'False'
											elif obj[12]>1.0:
												return 'True'
											else: return 'True'
										elif obj[11]<=1.0:
											return 'True'
										else: return 'True'
									elif obj[5]>6:
										return 'False'
									else: return 'False'
								else: return 'True'
							elif obj[0]<=0:
								return 'False'
							else: return 'False'
						elif obj[9]>6:
							return 'True'
						else: return 'True'
					elif obj[1]<=0:
						return 'False'
					else: return 'False'
				elif obj[8]<=5:
					return 'True'
				else: return 'True'
			elif obj[2]<=1:
				# {"feature": "Education", "instances": 6, "metric_value": 0.65, "depth": 4}
				if obj[7]>0:
					return 'False'
				elif obj[7]<=0:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[10]>2.0:
			return 'True'
		else: return 'True'
	elif obj[14]>2:
		# {"feature": "Age", "instances": 10, "metric_value": 0.8813, "depth": 2}
		if obj[5]<=1:
			# {"feature": "Coupon", "instances": 6, "metric_value": 1.0, "depth": 3}
			if obj[2]<=2:
				# {"feature": "Time", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[1]>0:
					return 'False'
				elif obj[1]<=0:
					return 'True'
				else: return 'True'
			elif obj[2]>2:
				return 'True'
			else: return 'True'
		elif obj[5]>1:
			return 'False'
		else: return 'False'
	else: return 'False'
