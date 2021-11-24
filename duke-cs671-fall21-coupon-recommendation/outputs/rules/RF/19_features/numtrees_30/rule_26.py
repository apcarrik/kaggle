def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Temperature, obj[3]: Time, obj[4]: Coupon, obj[5]: Coupon_validity, obj[6]: Gender, obj[7]: Age, obj[8]: Maritalstatus, obj[9]: Children, obj[10]: Education, obj[11]: Occupation, obj[12]: Income, obj[13]: Bar, obj[14]: Coffeehouse, obj[15]: Restaurantlessthan20, obj[16]: Restaurant20to50, obj[17]: Direction_same, obj[18]: Distance
	# {"feature": "Occupation", "instances": 34, "metric_value": 0.9774, "depth": 1}
	if obj[11]>3:
		# {"feature": "Coupon", "instances": 29, "metric_value": 0.9991, "depth": 2}
		if obj[4]>1:
			# {"feature": "Education", "instances": 24, "metric_value": 0.9544, "depth": 3}
			if obj[10]<=2:
				# {"feature": "Time", "instances": 18, "metric_value": 0.7642, "depth": 4}
				if obj[3]<=3:
					# {"feature": "Coupon_validity", "instances": 12, "metric_value": 0.9183, "depth": 5}
					if obj[5]>0:
						# {"feature": "Passanger", "instances": 9, "metric_value": 0.9911, "depth": 6}
						if obj[0]<=1:
							# {"feature": "Children", "instances": 5, "metric_value": 0.7219, "depth": 7}
							if obj[9]>0:
								return 'True'
							elif obj[9]<=0:
								# {"feature": "Maritalstatus", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[8]<=1:
									return 'False'
								elif obj[8]>1:
									return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[0]>1:
							# {"feature": "Age", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[7]<=2:
								return 'False'
							elif obj[7]>2:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[5]<=0:
						return 'True'
					else: return 'True'
				elif obj[3]>3:
					return 'True'
				else: return 'True'
			elif obj[10]>2:
				# {"feature": "Age", "instances": 6, "metric_value": 0.65, "depth": 4}
				if obj[7]<=6:
					return 'False'
				elif obj[7]>6:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[4]<=1:
			return 'False'
		else: return 'False'
	elif obj[11]<=3:
		return 'True'
	else: return 'True'
