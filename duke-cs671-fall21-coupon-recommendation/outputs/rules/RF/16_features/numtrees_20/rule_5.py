def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Children, obj[8]: Education, obj[9]: Occupation, obj[10]: Income, obj[11]: Bar, obj[12]: Coffeehouse, obj[13]: Restaurant20to50, obj[14]: Direction_same, obj[15]: Distance
	# {"feature": "Bar", "instances": 51, "metric_value": 0.9864, "depth": 1}
	if obj[11]<=2.0:
		# {"feature": "Restaurant20to50", "instances": 45, "metric_value": 0.9996, "depth": 2}
		if obj[13]<=1.0:
			# {"feature": "Education", "instances": 33, "metric_value": 0.9673, "depth": 3}
			if obj[8]<=3:
				# {"feature": "Occupation", "instances": 29, "metric_value": 0.9923, "depth": 4}
				if obj[9]>4:
					# {"feature": "Coffeehouse", "instances": 21, "metric_value": 0.9183, "depth": 5}
					if obj[12]<=2.0:
						# {"feature": "Age", "instances": 16, "metric_value": 0.9887, "depth": 6}
						if obj[6]<=4:
							# {"feature": "Time", "instances": 12, "metric_value": 0.9799, "depth": 7}
							if obj[2]<=2:
								# {"feature": "Coupon_validity", "instances": 9, "metric_value": 0.9911, "depth": 8}
								if obj[4]<=0:
									# {"feature": "Distance", "instances": 5, "metric_value": 0.7219, "depth": 9}
									if obj[15]<=2:
										return 'True'
									elif obj[15]>2:
										return 'False'
									else: return 'False'
								elif obj[4]>0:
									# {"feature": "Income", "instances": 4, "metric_value": 0.8113, "depth": 9}
									if obj[10]<=3:
										return 'False'
									elif obj[10]>3:
										return 'True'
									else: return 'True'
								else: return 'False'
							elif obj[2]>2:
								return 'False'
							else: return 'False'
						elif obj[6]>4:
							return 'True'
						else: return 'True'
					elif obj[12]>2.0:
						return 'True'
					else: return 'True'
				elif obj[9]<=4:
					# {"feature": "Coupon_validity", "instances": 8, "metric_value": 0.8113, "depth": 5}
					if obj[4]>0:
						return 'False'
					elif obj[4]<=0:
						# {"feature": "Passanger", "instances": 4, "metric_value": 1.0, "depth": 6}
						if obj[0]<=2:
							return 'True'
						elif obj[0]>2:
							return 'False'
						else: return 'False'
					else: return 'True'
				else: return 'False'
			elif obj[8]>3:
				return 'True'
			else: return 'True'
		elif obj[13]>1.0:
			# {"feature": "Passanger", "instances": 12, "metric_value": 0.8113, "depth": 3}
			if obj[0]<=1:
				# {"feature": "Age", "instances": 10, "metric_value": 0.469, "depth": 4}
				if obj[6]>1:
					return 'False'
				elif obj[6]<=1:
					# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[2]>1:
						return 'True'
					elif obj[2]<=1:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[0]>1:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[11]>2.0:
		return 'True'
	else: return 'True'
