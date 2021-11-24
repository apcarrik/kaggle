def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurantlessthan20, obj[15]: Restaurant20to50, obj[16]: Direction_same, obj[17]: Distance
	# {"feature": "Occupation", "instances": 34, "metric_value": 0.9082, "depth": 1}
	if obj[10]<=16:
		# {"feature": "Restaurantlessthan20", "instances": 30, "metric_value": 0.7838, "depth": 2}
		if obj[14]<=2.0:
			# {"feature": "Income", "instances": 19, "metric_value": 0.9495, "depth": 3}
			if obj[11]>1:
				# {"feature": "Children", "instances": 16, "metric_value": 0.8113, "depth": 4}
				if obj[8]<=0:
					# {"feature": "Coffeehouse", "instances": 9, "metric_value": 0.9911, "depth": 5}
					if obj[13]>1.0:
						# {"feature": "Time", "instances": 7, "metric_value": 0.8631, "depth": 6}
						if obj[2]>0:
							return 'True'
						elif obj[2]<=0:
							# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[0]>0:
								return 'False'
							elif obj[0]<=0:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[13]<=1.0:
						return 'False'
					else: return 'False'
				elif obj[8]>0:
					return 'True'
				else: return 'True'
			elif obj[11]<=1:
				return 'False'
			else: return 'False'
		elif obj[14]>2.0:
			return 'True'
		else: return 'True'
	elif obj[10]>16:
		return 'False'
	else: return 'False'
