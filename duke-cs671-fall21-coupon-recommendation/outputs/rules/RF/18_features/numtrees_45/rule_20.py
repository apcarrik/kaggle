def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurantlessthan20, obj[15]: Restaurant20to50, obj[16]: Direction_same, obj[17]: Distance
	# {"feature": "Coffeehouse", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[13]>0.0:
		# {"feature": "Passanger", "instances": 18, "metric_value": 0.8524, "depth": 2}
		if obj[0]<=2:
			# {"feature": "Time", "instances": 13, "metric_value": 0.9612, "depth": 3}
			if obj[2]<=3:
				# {"feature": "Age", "instances": 11, "metric_value": 0.8454, "depth": 4}
				if obj[6]>1:
					# {"feature": "Coupon", "instances": 6, "metric_value": 1.0, "depth": 5}
					if obj[3]>1:
						# {"feature": "Coupon_validity", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[4]<=0:
							return 'True'
						elif obj[4]>0:
							return 'False'
						else: return 'False'
					elif obj[3]<=1:
						return 'False'
					else: return 'False'
				elif obj[6]<=1:
					return 'True'
				else: return 'True'
			elif obj[2]>3:
				return 'False'
			else: return 'False'
		elif obj[0]>2:
			return 'True'
		else: return 'True'
	elif obj[13]<=0.0:
		return 'False'
	else: return 'False'
