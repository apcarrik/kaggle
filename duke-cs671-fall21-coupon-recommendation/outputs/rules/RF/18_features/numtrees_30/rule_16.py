def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurantlessthan20, obj[15]: Restaurant20to50, obj[16]: Direction_same, obj[17]: Distance
	# {"feature": "Age", "instances": 34, "metric_value": 0.9774, "depth": 1}
	if obj[6]>0:
		# {"feature": "Coupon_validity", "instances": 31, "metric_value": 0.9383, "depth": 2}
		if obj[4]<=0:
			# {"feature": "Time", "instances": 19, "metric_value": 0.7425, "depth": 3}
			if obj[2]<=1:
				# {"feature": "Education", "instances": 11, "metric_value": 0.9457, "depth": 4}
				if obj[9]<=0:
					# {"feature": "Restaurantlessthan20", "instances": 8, "metric_value": 1.0, "depth": 5}
					if obj[14]<=2.0:
						# {"feature": "Maritalstatus", "instances": 5, "metric_value": 0.7219, "depth": 6}
						if obj[7]>0:
							return 'True'
						elif obj[7]<=0:
							return 'False'
						else: return 'False'
					elif obj[14]>2.0:
						return 'False'
					else: return 'False'
				elif obj[9]>0:
					return 'True'
				else: return 'True'
			elif obj[2]>1:
				return 'True'
			else: return 'True'
		elif obj[4]>0:
			# {"feature": "Coffeehouse", "instances": 12, "metric_value": 0.9799, "depth": 3}
			if obj[13]>0.0:
				# {"feature": "Coupon", "instances": 9, "metric_value": 0.9911, "depth": 4}
				if obj[3]<=3:
					# {"feature": "Maritalstatus", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[7]>0:
						return 'True'
					elif obj[7]<=0:
						return 'False'
					else: return 'False'
				elif obj[3]>3:
					# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[0]<=1:
						return 'False'
					elif obj[0]>1:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[13]<=0.0:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[6]<=0:
		return 'False'
	else: return 'False'
