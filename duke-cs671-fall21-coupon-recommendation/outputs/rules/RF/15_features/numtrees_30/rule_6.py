def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Coupon_validity, obj[4]: Gender, obj[5]: Age, obj[6]: Children, obj[7]: Education, obj[8]: Occupation, obj[9]: Income, obj[10]: Bar, obj[11]: Coffeehouse, obj[12]: Restaurant20to50, obj[13]: Direction_same, obj[14]: Distance
	# {"feature": "Coupon", "instances": 34, "metric_value": 0.9367, "depth": 1}
	if obj[2]<=3:
		# {"feature": "Income", "instances": 22, "metric_value": 0.7732, "depth": 2}
		if obj[9]<=6:
			# {"feature": "Gender", "instances": 20, "metric_value": 0.6098, "depth": 3}
			if obj[4]>0:
				return 'True'
			elif obj[4]<=0:
				# {"feature": "Bar", "instances": 9, "metric_value": 0.9183, "depth": 4}
				if obj[10]>1.0:
					return 'True'
				elif obj[10]<=1.0:
					# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[0]<=2:
						return 'False'
					elif obj[0]>2:
						return 'True'
					else: return 'True'
				else: return 'False'
			else: return 'True'
		elif obj[9]>6:
			return 'False'
		else: return 'False'
	elif obj[2]>3:
		# {"feature": "Passanger", "instances": 12, "metric_value": 0.9799, "depth": 2}
		if obj[0]>1:
			# {"feature": "Children", "instances": 8, "metric_value": 0.9544, "depth": 3}
			if obj[6]<=0:
				# {"feature": "Occupation", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[8]<=7:
					return 'False'
				elif obj[8]>7:
					return 'True'
				else: return 'True'
			elif obj[6]>0:
				return 'True'
			else: return 'True'
		elif obj[0]<=1:
			return 'False'
		else: return 'False'
	else: return 'False'
