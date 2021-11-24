def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Income, obj[9]: Bar, obj[10]: Coffeehouse, obj[11]: Restaurant20to50, obj[12]: Direction_same, obj[13]: Distance
	# {"feature": "Coffeehouse", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[10]<=1.0:
		# {"feature": "Bar", "instances": 13, "metric_value": 0.8905, "depth": 2}
		if obj[9]<=1.0:
			# {"feature": "Income", "instances": 11, "metric_value": 0.684, "depth": 3}
			if obj[8]>0:
				# {"feature": "Restaurant20to50", "instances": 10, "metric_value": 0.469, "depth": 4}
				if obj[11]>-1.0:
					return 'False'
				elif obj[11]<=-1.0:
					return 'True'
				else: return 'True'
			elif obj[8]<=0:
				return 'True'
			else: return 'True'
		elif obj[9]>1.0:
			return 'True'
		else: return 'True'
	elif obj[10]>1.0:
		# {"feature": "Income", "instances": 10, "metric_value": 0.469, "depth": 2}
		if obj[8]<=6:
			return 'True'
		elif obj[8]>6:
			return 'False'
		else: return 'False'
	else: return 'True'
