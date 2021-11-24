def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Income, obj[9]: Bar, obj[10]: Coffeehouse, obj[11]: Restaurant20to50, obj[12]: Direction_same, obj[13]: Distance
	# {"feature": "Occupation", "instances": 34, "metric_value": 0.874, "depth": 1}
	if obj[7]<=7:
		# {"feature": "Coupon", "instances": 19, "metric_value": 0.4855, "depth": 2}
		if obj[2]>0:
			return 'True'
		elif obj[2]<=0:
			# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 3}
			if obj[0]>1:
				return 'False'
			elif obj[0]<=1:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[7]>7:
		# {"feature": "Bar", "instances": 15, "metric_value": 0.9968, "depth": 2}
		if obj[9]>0.0:
			# {"feature": "Age", "instances": 12, "metric_value": 0.9799, "depth": 3}
			if obj[4]<=1:
				# {"feature": "Income", "instances": 8, "metric_value": 0.9544, "depth": 4}
				if obj[8]>2:
					return 'False'
				elif obj[8]<=2:
					# {"feature": "Children", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[5]<=0:
						return 'True'
					elif obj[5]>0:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[4]>1:
				return 'True'
			else: return 'True'
		elif obj[9]<=0.0:
			return 'False'
		else: return 'False'
	else: return 'False'
