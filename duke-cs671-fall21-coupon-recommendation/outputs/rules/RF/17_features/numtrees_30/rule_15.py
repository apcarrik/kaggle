def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurant20to50, obj[15]: Direction_same, obj[16]: Distance
	# {"feature": "Restaurant20to50", "instances": 34, "metric_value": 0.9774, "depth": 1}
	if obj[14]>0.0:
		# {"feature": "Income", "instances": 29, "metric_value": 0.8936, "depth": 2}
		if obj[11]>3:
			# {"feature": "Age", "instances": 16, "metric_value": 1.0, "depth": 3}
			if obj[6]<=4:
				# {"feature": "Coupon", "instances": 13, "metric_value": 0.9612, "depth": 4}
				if obj[3]<=3:
					# {"feature": "Occupation", "instances": 9, "metric_value": 0.7642, "depth": 5}
					if obj[10]<=5:
						# {"feature": "Coffeehouse", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[13]<=2.0:
							# {"feature": "Weather", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[1]<=0:
								# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[0]<=1:
									return 'False'
								elif obj[0]>1:
									return 'True'
								else: return 'True'
							elif obj[1]>0:
								return 'True'
							else: return 'True'
						elif obj[13]>2.0:
							return 'False'
						else: return 'False'
					elif obj[10]>5:
						return 'True'
					else: return 'True'
				elif obj[3]>3:
					# {"feature": "Weather", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[1]<=0:
						return 'False'
					elif obj[1]>0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[6]>4:
				return 'False'
			else: return 'False'
		elif obj[11]<=3:
			# {"feature": "Occupation", "instances": 13, "metric_value": 0.3912, "depth": 3}
			if obj[10]<=11:
				return 'True'
			elif obj[10]>11:
				# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[0]>0:
					return 'False'
				elif obj[0]<=0:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'True'
	elif obj[14]<=0.0:
		return 'False'
	else: return 'False'
