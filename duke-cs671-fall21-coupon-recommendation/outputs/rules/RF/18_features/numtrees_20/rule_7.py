def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurantlessthan20, obj[15]: Restaurant20to50, obj[16]: Direction_same, obj[17]: Distance
	# {"feature": "Passanger", "instances": 51, "metric_value": 0.9975, "depth": 1}
	if obj[0]<=2:
		# {"feature": "Coupon_validity", "instances": 43, "metric_value": 0.9523, "depth": 2}
		if obj[4]<=0:
			# {"feature": "Occupation", "instances": 22, "metric_value": 0.976, "depth": 3}
			if obj[10]>1:
				# {"feature": "Coffeehouse", "instances": 17, "metric_value": 0.9975, "depth": 4}
				if obj[13]<=2.0:
					# {"feature": "Bar", "instances": 14, "metric_value": 0.9403, "depth": 5}
					if obj[12]>0.0:
						# {"feature": "Age", "instances": 10, "metric_value": 0.7219, "depth": 6}
						if obj[6]<=1:
							# {"feature": "Direction_same", "instances": 5, "metric_value": 0.971, "depth": 7}
							if obj[16]<=0:
								# {"feature": "Income", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[11]>0:
									return 'True'
								elif obj[11]<=0:
									return 'False'
								else: return 'False'
							elif obj[16]>0:
								return 'False'
							else: return 'False'
						elif obj[6]>1:
							return 'False'
						else: return 'False'
					elif obj[12]<=0.0:
						# {"feature": "Coupon", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[3]>0:
							return 'True'
						elif obj[3]<=0:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[13]>2.0:
					return 'True'
				else: return 'True'
			elif obj[10]<=1:
				return 'True'
			else: return 'True'
		elif obj[4]>0:
			# {"feature": "Income", "instances": 21, "metric_value": 0.5917, "depth": 3}
			if obj[11]>1:
				# {"feature": "Occupation", "instances": 17, "metric_value": 0.3228, "depth": 4}
				if obj[10]<=17:
					return 'False'
				elif obj[10]>17:
					# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[2]>0:
						return 'False'
					elif obj[2]<=0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[11]<=1:
				# {"feature": "Coupon", "instances": 4, "metric_value": 1.0, "depth": 4}
				if obj[3]<=1:
					return 'False'
				elif obj[3]>1:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'False'
	elif obj[0]>2:
		return 'True'
	else: return 'True'
