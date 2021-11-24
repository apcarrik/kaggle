def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Bar, obj[9]: Coffeehouse, obj[10]: Restaurant20to50, obj[11]: Direction_same, obj[12]: Distance
	# {"feature": "Bar", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[8]<=1.0:
		# {"feature": "Coffeehouse", "instances": 16, "metric_value": 0.896, "depth": 2}
		if obj[9]>0.0:
			return 'True'
		elif obj[9]<=0.0:
			# {"feature": "Coupon", "instances": 8, "metric_value": 0.9544, "depth": 3}
			if obj[2]<=2:
				return 'False'
			elif obj[2]>2:
				# {"feature": "Time", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[1]>0:
					return 'True'
				elif obj[1]<=0:
					return 'False'
				else: return 'False'
			else: return 'True'
		else: return 'False'
	elif obj[8]>1.0:
		return 'False'
	else: return 'False'
