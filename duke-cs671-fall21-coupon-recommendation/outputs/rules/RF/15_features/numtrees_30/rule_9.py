def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Coupon_validity, obj[4]: Gender, obj[5]: Age, obj[6]: Children, obj[7]: Education, obj[8]: Occupation, obj[9]: Income, obj[10]: Bar, obj[11]: Coffeehouse, obj[12]: Restaurant20to50, obj[13]: Direction_same, obj[14]: Distance
	# {"feature": "Coffeehouse", "instances": 34, "metric_value": 1.0, "depth": 1}
	if obj[11]<=1.0:
		# {"feature": "Restaurant20to50", "instances": 20, "metric_value": 0.8113, "depth": 2}
		if obj[12]>0.0:
			# {"feature": "Passanger", "instances": 16, "metric_value": 0.5436, "depth": 3}
			if obj[0]>0:
				# {"feature": "Income", "instances": 15, "metric_value": 0.3534, "depth": 4}
				if obj[9]<=5:
					return 'False'
				elif obj[9]>5:
					# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[1]<=2:
						return 'False'
					elif obj[1]>2:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[0]<=0:
				return 'True'
			else: return 'True'
		elif obj[12]<=0.0:
			# {"feature": "Time", "instances": 4, "metric_value": 0.8113, "depth": 3}
			if obj[1]<=2:
				return 'True'
			elif obj[1]>2:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[11]>1.0:
		# {"feature": "Children", "instances": 14, "metric_value": 0.5917, "depth": 2}
		if obj[6]<=0:
			return 'True'
		elif obj[6]>0:
			# {"feature": "Coupon", "instances": 4, "metric_value": 1.0, "depth": 3}
			if obj[2]>2:
				return 'True'
			elif obj[2]<=2:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'True'
