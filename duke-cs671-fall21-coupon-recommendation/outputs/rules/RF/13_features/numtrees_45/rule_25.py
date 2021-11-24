def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Bar, obj[9]: Coffeehouse, obj[10]: Restaurant20to50, obj[11]: Direction_same, obj[12]: Distance
	# {"feature": "Age", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[4]<=2:
		# {"feature": "Coffeehouse", "instances": 14, "metric_value": 0.9403, "depth": 2}
		if obj[9]<=2.0:
			# {"feature": "Children", "instances": 11, "metric_value": 0.994, "depth": 3}
			if obj[5]<=0:
				# {"feature": "Education", "instances": 6, "metric_value": 0.9183, "depth": 4}
				if obj[6]<=3:
					# {"feature": "Occupation", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[7]>5:
						return 'False'
					elif obj[7]<=5:
						return 'True'
					else: return 'True'
				elif obj[6]>3:
					return 'True'
				else: return 'True'
			elif obj[5]>0:
				# {"feature": "Education", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[6]>0:
					return 'True'
				elif obj[6]<=0:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[9]>2.0:
			return 'True'
		else: return 'True'
	elif obj[4]>2:
		# {"feature": "Direction_same", "instances": 9, "metric_value": 0.5033, "depth": 2}
		if obj[11]<=0:
			return 'False'
		elif obj[11]>0:
			return 'True'
		else: return 'True'
	else: return 'False'
