def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Children, obj[8]: Education, obj[9]: Occupation, obj[10]: Income, obj[11]: Bar, obj[12]: Coffeehouse, obj[13]: Restaurant20to50, obj[14]: Direction_same, obj[15]: Distance
	# {"feature": "Distance", "instances": 34, "metric_value": 0.7871, "depth": 1}
	if obj[15]<=2:
		# {"feature": "Occupation", "instances": 28, "metric_value": 0.5917, "depth": 2}
		if obj[9]<=11:
			# {"feature": "Age", "instances": 22, "metric_value": 0.2668, "depth": 3}
			if obj[6]>0:
				return 'True'
			elif obj[6]<=0:
				# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[0]<=1:
					return 'True'
				elif obj[0]>1:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[9]>11:
			# {"feature": "Bar", "instances": 6, "metric_value": 1.0, "depth": 3}
			if obj[11]<=2.0:
				# {"feature": "Coffeehouse", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[12]<=2.0:
					return 'False'
				elif obj[12]>2.0:
					return 'True'
				else: return 'True'
			elif obj[11]>2.0:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[15]>2:
		# {"feature": "Weather", "instances": 6, "metric_value": 0.9183, "depth": 2}
		if obj[1]>0:
			# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 3}
			if obj[2]>0:
				return 'True'
			elif obj[2]<=0:
				return 'False'
			else: return 'False'
		elif obj[1]<=0:
			return 'False'
		else: return 'False'
	else: return 'False'
