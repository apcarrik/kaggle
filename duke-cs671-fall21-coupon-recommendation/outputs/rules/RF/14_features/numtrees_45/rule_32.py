def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Income, obj[9]: Bar, obj[10]: Coffeehouse, obj[11]: Restaurant20to50, obj[12]: Direction_same, obj[13]: Distance
	# {"feature": "Education", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[6]>0:
		# {"feature": "Occupation", "instances": 14, "metric_value": 0.9403, "depth": 2}
		if obj[7]<=12:
			# {"feature": "Age", "instances": 10, "metric_value": 0.7219, "depth": 3}
			if obj[4]<=4:
				# {"feature": "Income", "instances": 9, "metric_value": 0.5033, "depth": 4}
				if obj[8]>0:
					return 'False'
				elif obj[8]<=0:
					return 'True'
				else: return 'True'
			elif obj[4]>4:
				return 'True'
			else: return 'True'
		elif obj[7]>12:
			# {"feature": "Children", "instances": 4, "metric_value": 0.8113, "depth": 3}
			if obj[5]<=0:
				return 'True'
			elif obj[5]>0:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[6]<=0:
		# {"feature": "Age", "instances": 9, "metric_value": 0.7642, "depth": 2}
		if obj[4]<=4:
			return 'True'
		elif obj[4]>4:
			# {"feature": "Gender", "instances": 4, "metric_value": 1.0, "depth": 3}
			if obj[3]<=0:
				return 'True'
			elif obj[3]>0:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'True'
