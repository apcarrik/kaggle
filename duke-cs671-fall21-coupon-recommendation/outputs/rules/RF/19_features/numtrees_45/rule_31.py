def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Temperature, obj[3]: Time, obj[4]: Coupon, obj[5]: Coupon_validity, obj[6]: Gender, obj[7]: Age, obj[8]: Maritalstatus, obj[9]: Children, obj[10]: Education, obj[11]: Occupation, obj[12]: Income, obj[13]: Bar, obj[14]: Coffeehouse, obj[15]: Restaurantlessthan20, obj[16]: Restaurant20to50, obj[17]: Direction_same, obj[18]: Distance
	# {"feature": "Passanger", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[0]<=2:
		# {"feature": "Restaurantlessthan20", "instances": 17, "metric_value": 0.9774, "depth": 2}
		if obj[15]<=2.0:
			# {"feature": "Coupon", "instances": 12, "metric_value": 0.9799, "depth": 3}
			if obj[4]>0:
				# {"feature": "Direction_same", "instances": 10, "metric_value": 0.8813, "depth": 4}
				if obj[17]<=0:
					# {"feature": "Bar", "instances": 8, "metric_value": 0.5436, "depth": 5}
					if obj[13]<=2.0:
						return 'True'
					elif obj[13]>2.0:
						return 'False'
					else: return 'False'
				elif obj[17]>0:
					return 'False'
				else: return 'False'
			elif obj[4]<=0:
				return 'False'
			else: return 'False'
		elif obj[15]>2.0:
			return 'False'
		else: return 'False'
	elif obj[0]>2:
		return 'True'
	else: return 'True'
