def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurantlessthan20, obj[15]: Restaurant20to50, obj[16]: Direction_same, obj[17]: Distance
	# {"feature": "Distance", "instances": 51, "metric_value": 0.8974, "depth": 1}
	if obj[17]<=2:
		# {"feature": "Occupation", "instances": 49, "metric_value": 0.8631, "depth": 2}
		if obj[10]<=14:
			# {"feature": "Coupon", "instances": 45, "metric_value": 0.8945, "depth": 3}
			if obj[3]>1:
				# {"feature": "Education", "instances": 30, "metric_value": 0.7838, "depth": 4}
				if obj[9]>1:
					# {"feature": "Weather", "instances": 17, "metric_value": 0.9367, "depth": 5}
					if obj[1]<=1:
						# {"feature": "Bar", "instances": 14, "metric_value": 0.9852, "depth": 6}
						if obj[12]<=1.0:
							# {"feature": "Age", "instances": 12, "metric_value": 0.9183, "depth": 7}
							if obj[6]<=4:
								# {"feature": "Passanger", "instances": 7, "metric_value": 0.5917, "depth": 8}
								if obj[0]<=2:
									return 'True'
								elif obj[0]>2:
									# {"feature": "Maritalstatus", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[7]<=0:
										return 'True'
									elif obj[7]>0:
										return 'False'
									else: return 'False'
								else: return 'True'
							elif obj[6]>4:
								# {"feature": "Coffeehouse", "instances": 5, "metric_value": 0.971, "depth": 8}
								if obj[13]>0.0:
									# {"feature": "Coupon_validity", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[4]<=0:
										return 'True'
									elif obj[4]>0:
										return 'False'
									else: return 'False'
								elif obj[13]<=0.0:
									return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[12]>1.0:
							return 'False'
						else: return 'False'
					elif obj[1]>1:
						return 'True'
					else: return 'True'
				elif obj[9]<=1:
					# {"feature": "Coffeehouse", "instances": 13, "metric_value": 0.3912, "depth": 5}
					if obj[13]<=3.0:
						return 'True'
					elif obj[13]>3.0:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[3]<=1:
				# {"feature": "Age", "instances": 15, "metric_value": 0.9968, "depth": 4}
				if obj[6]>0:
					# {"feature": "Coffeehouse", "instances": 13, "metric_value": 0.9612, "depth": 5}
					if obj[13]<=3.0:
						# {"feature": "Maritalstatus", "instances": 11, "metric_value": 0.8454, "depth": 6}
						if obj[7]<=1:
							return 'True'
						elif obj[7]>1:
							# {"feature": "Income", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[11]<=5:
								return 'False'
							elif obj[11]>5:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[13]>3.0:
						return 'False'
					else: return 'False'
				elif obj[6]<=0:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[10]>14:
			return 'True'
		else: return 'True'
	elif obj[17]>2:
		return 'False'
	else: return 'False'
