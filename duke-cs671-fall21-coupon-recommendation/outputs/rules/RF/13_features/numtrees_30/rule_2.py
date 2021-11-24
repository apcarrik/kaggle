def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Bar, obj[9]: Coffeehouse, obj[10]: Restaurant20to50, obj[11]: Direction_same, obj[12]: Distance
	# {"feature": "Passanger", "instances": 34, "metric_value": 0.99, "depth": 1}
	if obj[0]<=2:
		# {"feature": "Education", "instances": 25, "metric_value": 0.9896, "depth": 2}
		if obj[6]<=1:
			# {"feature": "Coupon", "instances": 13, "metric_value": 0.7793, "depth": 3}
			if obj[2]>2:
				# {"feature": "Age", "instances": 7, "metric_value": 0.9852, "depth": 4}
				if obj[4]<=3:
					# {"feature": "Coffeehouse", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[9]<=1.0:
						return 'False'
					elif obj[9]>1.0:
						return 'True'
					else: return 'True'
				elif obj[4]>3:
					return 'True'
				else: return 'True'
			elif obj[2]<=2:
				return 'False'
			else: return 'False'
		elif obj[6]>1:
			# {"feature": "Coupon", "instances": 12, "metric_value": 0.9183, "depth": 3}
			if obj[2]>2:
				# {"feature": "Occupation", "instances": 8, "metric_value": 1.0, "depth": 4}
				if obj[7]<=6:
					# {"feature": "Direction_same", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[11]<=0:
						return 'False'
					elif obj[11]>0:
						return 'True'
					else: return 'True'
				elif obj[7]>6:
					return 'True'
				else: return 'True'
			elif obj[2]<=2:
				return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[0]>2:
		# {"feature": "Occupation", "instances": 9, "metric_value": 0.5033, "depth": 2}
		if obj[7]<=21:
			return 'True'
		elif obj[7]>21:
			return 'False'
		else: return 'False'
	else: return 'True'
