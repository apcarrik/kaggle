def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurantlessthan20, obj[15]: Restaurant20to50, obj[16]: Direction_same, obj[17]: Distance
	# {"feature": "Age", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[6]<=4:
		# {"feature": "Occupation", "instances": 19, "metric_value": 0.998, "depth": 2}
		if obj[10]>1:
			# {"feature": "Coupon", "instances": 15, "metric_value": 0.971, "depth": 3}
			if obj[3]>1:
				# {"feature": "Weather", "instances": 10, "metric_value": 0.7219, "depth": 4}
				if obj[1]<=0:
					return 'True'
				elif obj[1]>0:
					# {"feature": "Income", "instances": 4, "metric_value": 1.0, "depth": 5}
					if obj[11]>4:
						return 'True'
					elif obj[11]<=4:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[3]<=1:
				# {"feature": "Income", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[11]>1:
					return 'False'
				elif obj[11]<=1:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[10]<=1:
			return 'False'
		else: return 'False'
	elif obj[6]>4:
		return 'True'
	else: return 'True'
