def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Temperature, obj[3]: Time, obj[4]: Coupon, obj[5]: Coupon_validity, obj[6]: Gender, obj[7]: Age, obj[8]: Maritalstatus, obj[9]: Children, obj[10]: Education, obj[11]: Occupation, obj[12]: Income, obj[13]: Bar, obj[14]: Coffeehouse, obj[15]: Restaurantlessthan20, obj[16]: Restaurant20to50, obj[17]: Direction_same, obj[18]: Distance
	# {"feature": "Education", "instances": 23, "metric_value": 0.9656, "depth": 1}
	if obj[10]<=2:
		# {"feature": "Children", "instances": 15, "metric_value": 0.971, "depth": 2}
		if obj[9]<=0:
			# {"feature": "Time", "instances": 10, "metric_value": 0.7219, "depth": 3}
			if obj[3]<=1:
				return 'True'
			elif obj[3]>1:
				# {"feature": "Age", "instances": 4, "metric_value": 1.0, "depth": 4}
				if obj[7]>1:
					return 'False'
				elif obj[7]<=1:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[9]>0:
			# {"feature": "Occupation", "instances": 5, "metric_value": 0.7219, "depth": 3}
			if obj[11]>1:
				return 'False'
			elif obj[11]<=1:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[10]>2:
		return 'False'
	else: return 'False'
