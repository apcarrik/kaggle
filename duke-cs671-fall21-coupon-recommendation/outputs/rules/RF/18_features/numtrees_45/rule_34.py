def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurantlessthan20, obj[15]: Restaurant20to50, obj[16]: Direction_same, obj[17]: Distance
	# {"feature": "Occupation", "instances": 23, "metric_value": 0.8865, "depth": 1}
	if obj[10]<=13:
		# {"feature": "Coffeehouse", "instances": 21, "metric_value": 0.7919, "depth": 2}
		if obj[13]<=3.0:
			# {"feature": "Restaurant20to50", "instances": 19, "metric_value": 0.6292, "depth": 3}
			if obj[15]<=3.0:
				# {"feature": "Bar", "instances": 18, "metric_value": 0.5033, "depth": 4}
				if obj[12]>0.0:
					return 'True'
				elif obj[12]<=0.0:
					# {"feature": "Children", "instances": 9, "metric_value": 0.7642, "depth": 5}
					if obj[8]>0:
						return 'True'
					elif obj[8]<=0:
						# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[0]<=1:
							return 'False'
						elif obj[0]>1:
							return 'True'
						else: return 'True'
					else: return 'False'
				else: return 'True'
			elif obj[15]>3.0:
				return 'False'
			else: return 'False'
		elif obj[13]>3.0:
			return 'False'
		else: return 'False'
	elif obj[10]>13:
		return 'False'
	else: return 'False'
