def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Income, obj[9]: Bar, obj[10]: Coffeehouse, obj[11]: Restaurant20to50, obj[12]: Direction_same, obj[13]: Distance
	# {"feature": "Coupon", "instances": 23, "metric_value": 0.8281, "depth": 1}
	if obj[2]<=2:
		# {"feature": "Age", "instances": 15, "metric_value": 0.971, "depth": 2}
		if obj[4]>2:
			# {"feature": "Restaurant20to50", "instances": 8, "metric_value": 0.5436, "depth": 3}
			if obj[11]>-1.0:
				return 'True'
			elif obj[11]<=-1.0:
				return 'False'
			else: return 'False'
		elif obj[4]<=2:
			# {"feature": "Income", "instances": 7, "metric_value": 0.8631, "depth": 3}
			if obj[8]>4:
				return 'False'
			elif obj[8]<=4:
				# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[0]<=1:
					return 'True'
				elif obj[0]>1:
					return 'False'
				else: return 'False'
			else: return 'True'
		else: return 'False'
	elif obj[2]>2:
		return 'True'
	else: return 'True'
