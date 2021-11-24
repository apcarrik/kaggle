def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Income, obj[9]: Bar, obj[10]: Coffeehouse, obj[11]: Restaurant20to50, obj[12]: Direction_same, obj[13]: Distance
	# {"feature": "Occupation", "instances": 34, "metric_value": 0.99, "depth": 1}
	if obj[7]<=7:
		# {"feature": "Passanger", "instances": 22, "metric_value": 0.8454, "depth": 2}
		if obj[0]<=2:
			# {"feature": "Direction_same", "instances": 17, "metric_value": 0.9367, "depth": 3}
			if obj[12]<=0:
				# {"feature": "Children", "instances": 12, "metric_value": 1.0, "depth": 4}
				if obj[5]<=0:
					# {"feature": "Distance", "instances": 8, "metric_value": 0.8113, "depth": 5}
					if obj[13]<=1:
						return 'True'
					elif obj[13]>1:
						# {"feature": "Coffeehouse", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[10]>0.0:
							return 'False'
						elif obj[10]<=0.0:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[5]>0:
					return 'False'
				else: return 'False'
			elif obj[12]>0:
				return 'True'
			else: return 'True'
		elif obj[0]>2:
			return 'True'
		else: return 'True'
	elif obj[7]>7:
		# {"feature": "Passanger", "instances": 12, "metric_value": 0.8113, "depth": 2}
		if obj[0]<=2:
			# {"feature": "Education", "instances": 7, "metric_value": 0.9852, "depth": 3}
			if obj[6]<=2:
				# {"feature": "Coupon", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[2]<=3:
					return 'True'
				elif obj[2]>3:
					return 'False'
				else: return 'False'
			elif obj[6]>2:
				return 'False'
			else: return 'False'
		elif obj[0]>2:
			return 'False'
		else: return 'False'
	else: return 'False'
