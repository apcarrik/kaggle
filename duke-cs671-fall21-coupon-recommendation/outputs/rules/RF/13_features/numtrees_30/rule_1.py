def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Bar, obj[9]: Coffeehouse, obj[10]: Restaurant20to50, obj[11]: Direction_same, obj[12]: Distance
	# {"feature": "Occupation", "instances": 34, "metric_value": 0.9082, "depth": 1}
	if obj[7]<=7:
		# {"feature": "Coupon", "instances": 26, "metric_value": 0.7063, "depth": 2}
		if obj[2]>0:
			# {"feature": "Restaurant20to50", "instances": 20, "metric_value": 0.2864, "depth": 3}
			if obj[10]>0.0:
				return 'True'
			elif obj[10]<=0.0:
				# {"feature": "Time", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[1]<=3:
					return 'True'
				elif obj[1]>3:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[2]<=0:
			# {"feature": "Age", "instances": 6, "metric_value": 0.9183, "depth": 3}
			if obj[4]<=2:
				return 'False'
			elif obj[4]>2:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[7]>7:
		# {"feature": "Children", "instances": 8, "metric_value": 0.8113, "depth": 2}
		if obj[5]<=0:
			return 'False'
		elif obj[5]>0:
			# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 3}
			if obj[2]>1:
				return 'True'
			elif obj[2]<=1:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'False'
