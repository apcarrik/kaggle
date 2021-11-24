def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Temperature, obj[3]: Time, obj[4]: Coupon, obj[5]: Coupon_validity, obj[6]: Gender, obj[7]: Age, obj[8]: Maritalstatus, obj[9]: Children, obj[10]: Education, obj[11]: Occupation, obj[12]: Income, obj[13]: Bar, obj[14]: Coffeehouse, obj[15]: Restaurantlessthan20, obj[16]: Restaurant20to50, obj[17]: Direction_same, obj[18]: Distance
	# {"feature": "Passanger", "instances": 34, "metric_value": 0.9975, "depth": 1}
	if obj[0]<=1:
		# {"feature": "Education", "instances": 19, "metric_value": 0.8315, "depth": 2}
		if obj[10]<=2:
			# {"feature": "Age", "instances": 12, "metric_value": 0.9799, "depth": 3}
			if obj[7]>1:
				# {"feature": "Coffeehouse", "instances": 7, "metric_value": 0.5917, "depth": 4}
				if obj[14]<=2.0:
					return 'False'
				elif obj[14]>2.0:
					return 'True'
				else: return 'True'
			elif obj[7]<=1:
				# {"feature": "Maritalstatus", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[8]<=0:
					return 'True'
				elif obj[8]>0:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[10]>2:
			return 'False'
		else: return 'False'
	elif obj[0]>1:
		# {"feature": "Coupon", "instances": 15, "metric_value": 0.5665, "depth": 2}
		if obj[4]<=3:
			return 'True'
		elif obj[4]>3:
			# {"feature": "Income", "instances": 4, "metric_value": 1.0, "depth": 3}
			if obj[12]>4:
				return 'True'
			elif obj[12]<=4:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'True'
