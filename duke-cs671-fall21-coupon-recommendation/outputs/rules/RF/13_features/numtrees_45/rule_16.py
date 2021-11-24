def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Bar, obj[9]: Coffeehouse, obj[10]: Restaurant20to50, obj[11]: Direction_same, obj[12]: Distance
	# {"feature": "Distance", "instances": 23, "metric_value": 0.8865, "depth": 1}
	if obj[12]<=2:
		# {"feature": "Passanger", "instances": 20, "metric_value": 0.7219, "depth": 2}
		if obj[0]<=1:
			# {"feature": "Age", "instances": 12, "metric_value": 0.9183, "depth": 3}
			if obj[4]>2:
				# {"feature": "Occupation", "instances": 7, "metric_value": 0.5917, "depth": 4}
				if obj[7]<=9:
					return 'True'
				elif obj[7]>9:
					return 'False'
				else: return 'False'
			elif obj[4]<=2:
				# {"feature": "Bar", "instances": 5, "metric_value": 0.971, "depth": 4}
				if obj[8]<=1.0:
					# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[2]<=2:
						return 'True'
					elif obj[2]>2:
						return 'False'
					else: return 'False'
				elif obj[8]>1.0:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[0]>1:
			return 'True'
		else: return 'True'
	elif obj[12]>2:
		return 'False'
	else: return 'False'
